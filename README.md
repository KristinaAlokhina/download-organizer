An automated Python script designed to clean up and structure the Windows Downloads folder by automatically categorizing files.

## 🚀 Features
- Automatic Sorting: Scans the Downloads folder and groups files by type (Images, Documents, Scripts, Installers).
- Dynamic Path Detection: Automatically detects the active Windows user's path using the `USERPROFILE` system environment variable.
- Standalone App: Can be compiled into a single `.exe` executable using PyInstaller, removing any Python environment dependencies.

## 🛠️ Technologies
- Python 3.14+
- Built-in modules: `os`, `shutil`, `sys`
- External libraries: `PyInstaller` (for the build process)

## 📦 Installation & Setup
1. Clone the repository:
   git clone https://github.com/KristinaAlokhina/download-organizer.git
2. Run the script:
   python organizer.py

Alternatively, compile the script into a standalone executable:

python -m PyInstaller --onefile --noconsole organizer.py