# app/gui.py

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from app.core import ImageViewerCore
import os
from PIL import Image, ImageTk

def launch_gui():
    root = tk.Tk()
    root.title("Nova - Image Viewer")
    root.geometry("1000x650")
    root.configure(bg="#121212")
    
    # --------------- Functions --------------- #
    def open_image():
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif *.webp"),
                ("All Files", "*.*")
            ]
        )
        if file_path:
            err = viewer.load_image(file_path)
            if err:
                messagebox.showerror("Error", f"Couldn't open image:\n{err}")

    def save_image():
        if not viewer.original_img:
            messagebox.showwarning("No Image", "No image to save")
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("PNG Image", "*.png"),
                ("JPEG Image", "*.jpg;*.jpeg"),
                ("BMP Image", "*.bmp"),
                ("All Files", "*.*")
            ]
        )
        if file_path:
            try:
                viewer.save_as(file_path)
                info_label.config(text=f"Image saved to: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Couldn't save:\n{e}")

    def on_resize(event):
        """Handle window resize"""
        canvas.coords(image_window, (canvas.winfo_width() // 2, 0))
        viewer.on_resize()
        canvas.configure(scrollregion=canvas.bbox("all"))

    # Set application icon
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(current_dir, '..', 'assets')
        logo_path = os.path.join(assets_dir, 'logo.png')
        
        # Load and resize logo for window icon
        img = Image.open(logo_path)
        img = img.resize((256, 256), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        root.wm_iconphoto(True, photo)
    except Exception as e:
        print(f"Could not load logo: {e}")

    # Enhanced Button Theme
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", 
                   font=("Segoe UI", 10), 
                   padding=8,
                   background="#333333", 
                   foreground="white",
                   bordercolor="#444444",
                   relief="flat")
    style.map("TButton",
              background=[("active", "#444444"), ("disabled", "#252525")],
              foreground=[("disabled", "#777777")])

    # Navigation Top Bar with Logo
    nav_frame = tk.Frame(root, bg="#1a1a1a", height=50)
    nav_frame.pack(fill="x", padx=0, pady=0)
    
    try:
        # Add logo to navbar
        logo_img = Image.open(os.path.join(assets_dir, 'logo.png'))
        logo_img = logo_img.resize((32, 32), Image.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(nav_frame, image=logo_photo, bg="#1a1a1a")
        logo_label.image = logo_photo
        logo_label.pack(side="left", padx=(15, 10), pady=5)
    except:
        pass

    # Canvas Area with improved scroll handling
    canvas_frame = tk.Frame(root, bg="#121212")
    canvas_frame.pack(fill="both", expand=True, padx=5, pady=5)

    canvas = tk.Canvas(canvas_frame, bg="#121212", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    # Scrollbars
    scroll_y = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
    scroll_y.pack(side="right", fill="y")
    scroll_x = ttk.Scrollbar(root, orient="horizontal", command=canvas.xview)
    scroll_x.pack(fill="x")
    
    canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    # Image container
    image_container = tk.Frame(canvas, bg="#121212")
    image_window = canvas.create_window((0, 0), window=image_container, anchor="nw")

    # Image label with improved event handling
    image_label = tk.Label(image_container, bg="#121212", cursor="arrow")
    image_label.pack()

    # Enhanced status bar
    status_frame = tk.Frame(root, bg="#1a1a1a", height=22)
    status_frame.pack(fill="x", side="bottom")
    
    info_label = tk.Label(status_frame, 
                         text="Ready", 
                         font=("Consolas", 9),
                         bg="#1a1a1a", 
                         fg="#aaaaaa",
                         anchor="w")
    info_label.pack(fill="x", padx=10)

    # Initialize Core Logic
    viewer = ImageViewerCore(canvas, image_label, info_label)
    viewer.set_image_window(image_window)

    # --------------- Menu System --------------- #
    menubar = tk.Menu(root, bg="#252525", fg="white", activebackground="#444")
    
    # File menu
    file_menu = tk.Menu(menubar, tearoff=0, bg="#252525", fg="white", activebackground="#444")
    file_menu.add_command(label="Open", command=open_image, accelerator="Ctrl+O")
    file_menu.add_command(label="Save As", command=save_image, accelerator="Ctrl+S")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=file_menu)
    
    # View menu
    view_menu = tk.Menu(menubar, tearoff=0, bg="#252525", fg="white", activebackground="#444")
    view_menu.add_command(label="Zoom In", command=viewer.zoom_in, accelerator="Ctrl++")
    view_menu.add_command(label="Zoom Out", command=viewer.zoom_out, accelerator="Ctrl+-")
    view_menu.add_command(label="Reset Zoom", command=viewer.reset_zoom, accelerator="Ctrl+0")
    view_menu.add_separator()
    view_menu.add_command(label="Rotate 90°", command=viewer.rotate_image, accelerator="Ctrl+R")
    menubar.add_cascade(label="View", menu=view_menu)
    
    root.config(menu=menubar)

    # --------------- Toolbar Buttons --------------- #
    btn_frame = tk.Frame(nav_frame, bg="#1a1a1a")
    btn_frame.pack(side="left", padx=10)
    
    ttk.Button(btn_frame, text="Open", command=open_image).pack(side="left", padx=2)
    ttk.Button(btn_frame, text="Save", command=save_image).pack(side="left", padx=2)
    
    zoom_frame = tk.Frame(nav_frame, bg="#1a1a1a")
    zoom_frame.pack(side="left", padx=10)
    
    ttk.Button(zoom_frame, text="+", command=viewer.zoom_in, width=3).pack(side="left", padx=1)
    ttk.Button(zoom_frame, text="-", command=viewer.zoom_out, width=3).pack(side="left", padx=1)
    ttk.Button(zoom_frame, text="1:1", command=viewer.reset_zoom, width=3).pack(side="left", padx=1)
    
    ttk.Button(nav_frame, text="Rotate", command=viewer.rotate_image).pack(side="left", padx=10)

    # --------------- Key Bindings --------------- #
    root.bind("<Control-o>", lambda e: open_image())
    root.bind("<Control-s>", lambda e: save_image())
    root.bind("<Control-plus>", lambda e: viewer.zoom_in())
    root.bind("<Control-minus>", lambda e: viewer.zoom_out())
    root.bind("<Control-0>", lambda e: viewer.reset_zoom())
    root.bind("<Control-r>", lambda e: viewer.rotate_image())
    
    # Configure canvas resizing
    canvas.bind("<Configure>", on_resize)
    
    # Launch GUI
    root.mainloop()