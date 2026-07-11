# Download Organizer

<p align="center">
  <a href="#-deutsch">Deutsch</a> • 
  <a href="#-english">English</a>
</p>

---

## 🇩🇪 Deutsch

### 🚀 Funktionen
* **Automatische Sortierung**: Scannt den Download-Ordner und sortiert Dateien nach Typen (Bilder, Dokumente, Skripte, Installer).
* **Dynamic Path Detection**: Erkennt automatisch den Pfad des aktuellen Windows-Benutzers über Systemvariablen (`USERPROFILE`).
* **Standalone App**: Kann mit PyInstaller in eine eigenständige `.exe`-Datei ohne Python-Abhängigkeiten kompiliert werden.

### 🛠️ Technologien
* Python 3.10+
* Integrierte Module: `os`, `shutil`, `sys`
* Externe Bibliotheken: `PyInstaller` (für den Build-Prozess)

### 📦 Installation & Start
1. Repository klonen:
   ```bash
   git clone https://github.com
   ```
2. Skript ausführen:
   ```bash
   python organizer.py
   ```

Alternativ kann das Skript als ausführbare Datei kompiliert werden:
```bash
python -m PyInstaller --onefile --noconsole organizer.py
```

---

## 🇺🇸 English

### 🚀 Features
* **Automatic Sorting**: Scans the Downloads folder and groups files by type (Images, Documents, Scripts, Installers, Music, Videos).
* **Dynamic Path Detection**: Automatically detects the active Windows user's path using the `USERPROFILE` system environment variable.
* **Standalone App**: Can be compiled into a single `.exe` executable using PyInstaller, removing any Python environment dependencies.

### 🛠️ Technologies
* Python 3.14+
* Built-in modules: `os`, `shutil`, `sys`
* External libraries: `PyInstaller` (for the build process)

### 📦 Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Run the script:
   ```bash
   python organizer.py
   ```

Alternatively, compile the script into a standalone executable:
```bash
python -m PyInstaller --onefile --noconsole organizer.py
```
