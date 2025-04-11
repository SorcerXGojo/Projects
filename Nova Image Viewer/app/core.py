# app/core.py

from PIL import Image, ImageTk, ImageDraw

class ImageViewerCore:
    def __init__(self, canvas, image_label, info_label):
        # Core state variables
        self.original_img = None
        self.display_img = None
        self.tk_img = None
        self.zoom_factor = 1.0
        self.base_scale = 1.0
        self.current_rotation = 0
        self.pan_start = None
        self.selection_rect = None
        self.selection_start = None
        self.last_mouse_pos = None

        # Widgets
        self.canvas = canvas
        self.image_label = image_label
        self.info_label = info_label
        self.image_window = None

        # Initialize mouse controls
        self.setup_mouse_controls()

    def setup_mouse_controls(self):
        """Initialize all mouse event bindings"""
        # Panning controls
        self.canvas.bind("<ButtonPress-1>", self.start_pan)
        self.canvas.bind("<B1-Motion>", self.pan_image)
        self.canvas.bind("<ButtonRelease-1>", self.end_pan)
        
        # Zoom controls
        self.canvas.bind("<MouseWheel>", self.mouse_wheel_zoom)
        self.canvas.bind("<Control-Button-4>", lambda e: self.zoom_in())  # Linux zoom in
        self.canvas.bind("<Control-Button-5>", lambda e: self.zoom_out())  # Linux zoom out
        
        # Selection controls
        self.canvas.bind("<ButtonPress-3>", self.start_selection)
        self.canvas.bind("<B3-Motion>", self.update_selection)
        self.canvas.bind("<ButtonRelease-3>", self.end_selection)
        
        # Mouse position tracking
        self.canvas.bind("<Motion>", self.track_mouse_position)

    def set_image_window(self, window_id):
        self.image_window = window_id

    def get_fit_scale(self, img):
        """Calculate initial scale to fit image within canvas size"""
        self.canvas.update_idletasks()
        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        return min((w - 50) / img.width, (h - 50) / img.height, 1.0)

    def load_image(self, file_path):
        """Open and load image from file"""
        try:
            self.original_img = Image.open(file_path)
            self.display_img = self.original_img.copy()
            self.zoom_factor = 1.0
            self.current_rotation = 0
            self.base_scale = self.get_fit_scale(self.original_img)
            self.update_display()
            self.info_label.config(text=f"🖼️ Loaded: {file_path} | {self.original_img.size[0]}×{self.original_img.size[1]}")
        except Exception as e:
            return str(e)
        return None

    def update_display(self):
        """Redraw image on the canvas"""
        if not self.original_img:
            return

        # Apply rotation if needed
        if self.current_rotation != 0:
            self.display_img = self.original_img.rotate(self.current_rotation, expand=True)
        else:
            self.display_img = self.original_img.copy()

        # Apply zoom
        scale = self.base_scale * self.zoom_factor
        new_size = (int(self.display_img.width * scale), int(self.display_img.height * scale))
        resized_img = self.display_img.resize(new_size, Image.LANCZOS)

        # Convert to Tkinter PhotoImage
        self.tk_img = ImageTk.PhotoImage(resized_img)
        self.image_label.config(image=self.tk_img)
        self.image_label.image = self.tk_img

        # Update canvas
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.canvas.coords(self.image_window, (self.canvas.winfo_width() // 2, 0))

    # Mouse Control Methods
    def start_pan(self, event):
        """Begin dragging the image"""
        self.pan_start = (event.x, event.y)
        self.canvas.config(cursor="hand2")

    def pan_image(self, event):
        """Drag the image"""
        if self.pan_start:
            dx = event.x - self.pan_start[0]
            dy = event.y - self.pan_start[1]
            self.canvas.move(self.image_window, dx, dy)
            self.pan_start = (event.x, event.y)

    def end_pan(self, event):
        """End dragging"""
        self.canvas.config(cursor="")
        self.pan_start = None

    def mouse_wheel_zoom(self, event):
        """Zoom in/out with mouse wheel"""
        if event.state & 0x4:  # Ctrl key pressed
            if event.delta > 0:
                self.zoom_in()
            else:
                self.zoom_out()
        else:
            # Regular scrolling
            self.canvas.yview_scroll(int(-1*(event.delta / 120)), "units")

    def start_selection(self, event):
        """Begin rectangular selection"""
        self.selection_start = (event.x, event.y)
        self.selection_rect = self.canvas.create_rectangle(
            event.x, event.y, event.x, event.y,
            outline="red", dash=(4,4), width=2, tag="selection")

    def update_selection(self, event):
        """Update selection rectangle"""
        if self.selection_rect:
            self.canvas.coords(self.selection_rect,
                             self.selection_start[0], self.selection_start[1],
                             event.x, event.y)

    def end_selection(self, event):
        """Finalize selection and crop image"""
        if self.selection_rect and self.selection_start:
            x1, y1, x2, y2 = self.canvas.coords(self.selection_rect)
            self.crop_image((x1, y1, x2, y2))
            self.canvas.delete(self.selection_rect)
            self.selection_rect = None
            self.selection_start = None

    def track_mouse_position(self, event):
        """Update mouse position in status bar"""
        self.last_mouse_pos = (event.x, event.y)
        if self.original_img:
            img_x = int((event.x - self.canvas.winfo_width()/2) / (self.base_scale * self.zoom_factor))
            img_y = int(event.y / (self.base_scale * self.zoom_factor))
            self.info_label.config(
                text=f"Mouse: {event.x},{event.y} | Image: {img_x},{img_y} | "
                     f"Zoom: {int(self.zoom_factor*100)}% | "
                     f"Size: {self.original_img.size[0]}×{self.original_img.size[1]}")

    # Image Manipulation Methods
    def zoom_in(self):
        self.zoom_factor = min(self.zoom_factor + 0.1, 5.0)  # Max 500% zoom
        self.update_display()

    def zoom_out(self):
        self.zoom_factor = max(self.zoom_factor - 0.1, 0.1)  # Min 10% zoom
        self.update_display()

    def reset_zoom(self):
        """Reset zoom to fit window"""
        self.zoom_factor = 1.0
        self.base_scale = self.get_fit_scale(self.original_img)
        self.update_display()

    def rotate_image(self):
        """Rotate image clockwise by 90°"""
        self.current_rotation = (self.current_rotation + 90) % 360
        self.update_display()

    def crop_image(self, coordinates):
        """Crop image based on selection coordinates"""
        if not self.original_img:
            return

        # Convert canvas coordinates to image coordinates
        scale = self.base_scale * self.zoom_factor
        x1 = int((coordinates[0] - self.canvas.winfo_width()/2) / scale)
        y1 = int(coordinates[1] / scale)
        x2 = int((coordinates[2] - self.canvas.winfo_width()/2) / scale)
        y2 = int(coordinates[3] / scale)

        # Ensure coordinates are within image bounds
        w, h = self.display_img.size
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(w, x2), min(h, y2)

        if x2 > x1 and y2 > y1:  # Valid selection
            self.original_img = self.display_img.crop((x1, y1, x2, y2))
            self.reset_zoom()

    def save_as(self, file_path):
        """Save current original image"""
        if self.original_img:
            self.original_img.save(file_path)

    def on_resize(self):
        """Update image size on canvas resize"""
        if self.original_img:
            if self.zoom_factor == 1.0:  # Only auto-resize if at 100% zoom
                self.base_scale = self.get_fit_scale(self.original_img)
            self.update_display()