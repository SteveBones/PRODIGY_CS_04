# Modern Python Keylogger (Educational)

A lightweight, modern-looking keylogger built with Python using **CustomTkinter** for the GUI and **pynput** for keystroke capturing. This project is designed for educational purposes to demonstrate how event listeners and background threading work in Python.

---

## ⚠️ ETHICAL DISCLAIMER
**This tool is for educational and ethical testing purposes only.** 
*   **NEVER** install or run this software on a computer you do not own or have explicit permission to monitor.
*   Unauthorized use of keyloggers is illegal and a violation of privacy laws.
*   The author is not responsible for any misuse of this software.

---

## Features
- **Modern UI:** Built with `CustomTkinter` featuring a dark mode interface.
- **Background Threading:** The keylogger runs on a separate thread to keep the GUI responsive.
- **Human-Readable Logs:** Automatically converts special keys like `[SPACE]`, `[ENTER]`, and `[BACKSPACE]` for better readability.
- **Start/Stop Control:** Easily control when recording is active via the GUI buttons.

## Prerequisites
- **Python 3.7+**
- **pip** (Python package manager)

## Installation

1. **Clone or create the project folder:**
   ```bash
   mkdir ModernKeylogger
   cd ModernKeylogger
   ```

2. **Install the required libraries:**
   ```bash
   pip install pynput customtkinter
   ```

## Usage

1. **Open the project in VS Code:**
   - Launch VS Code and open the `ModernKeylogger` folder.
   - Open `main.py`.

2. **Run the application:**
   - Click the **Run** button in VS Code or type the following in the terminal:
     ```bash
     python main.py
     ```

3. **Operate the UI:**
   - Click **Start Logging** to begin capturing keystrokes.
   - Click **Stop Logging** to save and end the session.
   - The keystrokes will be saved to a file named `keylog.txt` in the same directory.

## Troubleshooting

- **Antivirus Flags:** Because this script monitors keyboard input, your antivirus (like Windows Defender) may flag it as a threat. You may need to temporarily allow the script to run for testing.
- **File Permissions:** Ensure the script has permission to write files in the folder where it is located.

## License
Distributed under the MIT License. Use responsibly.
```

### How to view this in VS Code:
1.  After you create the `README.md` file and paste the code, you can see a "live preview."
2.  Right-click the `README.md` file in the explorer.
3.  Select **Open Preview** (or press `Ctrl+Shift+V`). 
4.  This will show you the formatted version with bold headers and clean code blocks.
