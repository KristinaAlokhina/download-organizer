# Download Organizer

<p align="center">
  <a href="#-deutsch">Deutsch</a> • 
  <a href="#-english">English</a>
</p>


---

## 🇩🇪 Deutsch


### 🚀 Funktionen
* **Automatische Sortierung**: Scannt den Download-Ordner und sortiert Mediendateien, Dokumente und Installer in entsprechende Unterordner.
* **Erweiterte Protokollierung**: Erstellt detaillierte Berichte im Ordner `Download_Organizer_Logs` im Benutzerverzeichnis.
* **Prozess-Statistik**: Zählt erfolgreiche, nicht unterstützte und fehlgeschlagene Dateiverschiebungen für maximale Transparenz.
* **Sicherheits-Schutz**: Ignoriert automatisch die aktuell ausgeführte Skript- oder `.exe`-Datei, um Fehler zu vermeiden.
* **Dynamic Path Detection**: Erkennt den Windows-Benutzerpfad automatisch über die Umgebungsvariable `USERPROFILE`.

### 🛠️ Technologien
* Python 3.10+
* Integrierte Module: `os`, `shutil`, `sys`, `datetime`
* Externe Bibliotheken: `PyInstaller` (optional für den Build-Prozess)

### 📂 Struktur der Dateisortierung
Das Skript sortiert Dateien nach folgenden Kategorien:
* **Bilder**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`
* **Dokumente**: `.pdf`, `.docx`, `.xlsx`, `.txt`, `.pptx`
* **Skripte**: `.py`, `.cs`, `.sh`, `.bat`
* **Installer**: `.exe`, `.msi`, `.zip`, `.rar`
* **Musik**: `.mp3`, `.wav`, `.flac`, `.aac`
* **Videos**: `.mp4`, `.avi`, `.mkv`, `.mov`

### 📦 Installation & Start
1. Repository klonen:
   ```bash
   git clone https://github.com/KristinaAlokhina/download-organizer
   ```
2. Skript ausführen:
   ```bash
   python Organizer.py
   ```

Alternativ kann das Skript als eigenständige Windows-Anwendung kompiliert werden:
```bash
python -m PyInstaller --onefile --noconsole Organizer.py
```

---

## 🇺🇸 English


### 🚀 Features
* **Automatic Sorting**: Scans the Downloads folder and groups media files, documents, and installers into designated subfolders.
* **Advanced Logging**: Generates detailed sorting reports inside the `Download_Organizer_Logs` directory in the user profile.
* **Process Statistics**: Tracks successful, unsupported, and failed file movements for full transparency.
* **Self-Protection**: Automatically ignores the currently running script or `.exe` file to prevent errors.
* **Dynamic Path Detection**: Automatically detects the Windows user path using the `USERPROFILE` environment variable.

### 🛠️ Technologies
* Python 3.10+ (Built with modern built-in libraries)
* Built-in modules: `os`, `shutil`, `sys`, `datetime`
* External libraries: `PyInstaller` (optional for the build process)

### 📂 File Sorting Structure
The script categorizes files based on the following extensions:
* **Images (Bilder)**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`
* **Documents (Dokumente)**: `.pdf`, `.docx`, `.xlsx`, `.txt`, `.pptx`
* **Scripts (Skripte)**: `.py`, `.cs`, `.sh`, `.bat`
* **Installers (Installer)**: `.exe`, `.msi`, `.zip`, `.rar`
* **Music (Musik)**: `.mp3`, `.wav`, `.flac`, `.aac`
* **Videos (Videos)**: `.mp4`, `.avi`, `.mkv`, `.mov`

### 📦 Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/KristinaAlokhina/download-organizer
   ```
2. Run the script:
   ```bash
   python Organizer.py
   ```

Alternatively, compile the script into a standalone Windows executable:
```bash
python -m PyInstaller --onefile --noconsole Organizer.py
```
