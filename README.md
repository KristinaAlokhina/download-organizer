<p align="center">
  <ins><b><kbd>&nbsp;DESKTOP APPLICATION&nbsp;</kbd></b></ins>
</p>

<h1 align="center" style="font-size: 2.5rem; font-weight: 900; color: #1a1a1a; margin-top: 10px; margin-bottom: 10px; border-bottom: none;">
  🎯 DOWNLOAD ORGANIZER (v3.0)
</h1>

<p align="center">
  <strong>Ein intelligenter, automatisierter Datei-Sortierer mit einer modernen grafischen Benutzeroberfläche.</strong>
  <br />
  <i>Entwickelt mit Python, Tkinter und Multithreading für eine nahtlose Hintergrundüberwachung.</i>
</p>

<p align="center">
  <a href="#-deutsch">🇩🇪 Deutsch</a> • 
  <a href="#-english">🇺🇸 English</a>
</p>

---

## 🇩🇪 Deutsch

Die Anwendung bietet eine intuitive, flache Benutzeroberfläche (Flat-UI) zur automatischen Organisation Ihres Download-Ordners. Sie läuft unauffällig im Hintergrund und sortiert Dateien basierend auf ihren Endungen in logische Unterordner.

### 🚀 Funktionen
* **Modernes Flat-Design (UI/UX)**: Farbkodierte Buttons und eine strukturierte Oberfläche für maximale Übersichtlichkeit.
* **Echtzeit-Log-Konsole 📝**: Integrierte, farblich hervorgehobene Konsole (Erfolg, Warnung, Fehler, Info), die jede Dateiaktion live protokolliert.
* **Intelligenter Hintergrundmodus 🔄**: Überwacht den Ordner im 10-Sekunden-Takt über einen separaten Thread, ohne die Benutzeroberfläche einzufrieren.
* **Sicherheitsschutz vor Blockaden 🔒**: Erkennt automatisch, ob eine Datei noch heruntergeladen wird, und wartet, bis das System sie freigibt.
* **Auto-Skript-Ausschluss**: Das Tool ignoriert sich selbst, falls es direkt im Download-Ordner ausgeführt wird.

### 🛠️ Technologien
* **GUI-Framework**: Python Tkinter (mit modernen `ttk`-Themen-Styles)
* **Prozess-Logik**: `shutil` (Dateiverschiebung), `os.scandir` (Performantes Verzeichnis-Scanning)
* **Asynchronität**: `threading` (Multithreading für blockierungsfreie GUI-Schleifen)

### 📂 Unterstützte Dateitypen & Ordnerstruktur
Das Programm scannt das Verzeichnis und sortiert Dateien in folgende Zielordner:
* **`Bilder/`**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.webp`
* **`Dokumente/`**: `.pdf`, `.docx`, `.xlsx`, `.txt`, `.pptx`, `.csv`
* **`Skripte/`**: `.py`, `.cs`, `.sh`, `.bat`, `.json`, `.html`, `.css`
* **`Installer/`**: `.exe`, `.msi`, `.zip`, `.rar`, `.7z`
* **`Musik/`**: `.mp3`, `.wav`, `.flac`, `.aac`
* **`Videos/`**: `.mp4`, `.avi`, `.mkv`, `.mov`

### 📦 Installation & Ausführung

#### Voraussetzungen
Es wird lediglich eine installierte Python 3.x Umgebung benötigt (Tkinter ist standardmäßig in Python enthalten).

1. Repository klonen oder Skript herunterladen:
   ```bash
   git clone https://github.comhttps://github.com/KristinaAlokhina/download-organizer
   ```
2. In den Projektordner wechseln:
   ```bash
   cd download_organizer
   ```
3. Die Anwendung starten:
   ```bash
   Organizer.py
   ```

---

## 🇺🇸 English

A smart, lightweight desktop utility featuring a modern Flat-UI to keep your user downloads folder structured, clean, and completely automated.

### 🚀 Features
* **Modern Flat Design (UI/UX)**: Styled with clear, color-coded interactive action buttons and a clean workspace.
* **Real-time Log Console 📝**: Built-in dark-themed console with advanced text-tag coloring (`Success`, `Warning`, `Error`, `Info`) for direct visual feedback.
* **Asynchronous Background Monitor 🔄**: Runs a discrete file-system watcher in a separate daemon thread without locking or freezing the main interface.
* **File-Lock Safety Measures 🔒**: Proactively checks if temporary system streams are still writing data (e.g., active browser downloads) before attempting moves.
* **Self-Exclusion Mechanism**: Smart logic skips the main execution script automatically if saved directly within the target directory.

### 🛠️ Technologies
* **GUI Framework**: Python Tkinter (enhanced via modular `ttk` flat-styling configurations)
* **Core Logic**: `shutil` (high-level file operations), `os.scandir` (optimized directory traversal)
* **Concurrency**: `threading` (Multi-threaded loop workflows)

### 📂 Supported File Categories & Destinations
Files are safely evaluated and sorted into dedicated directories based on extension maps:
* **`Bilder (Images)/`**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.webp`
* **`Dokumente (Documents)/`**: `.pdf`, `.docx`, `.xlsx`, `.txt`, `.pptx`, `.csv`
* **`Skripte (Scripts)/`**: `.py`, `.cs`, `.sh`, `.bat`, `.json`, `.html`, `.css`
* **`Installer (Archives)/`**: `.exe`, `.msi`, `.zip`, `.rar`, `.7z`
* **`Musik (Audio)/`**: `.mp3`, `.wav`, `.flac`, `.aac`
* **`Videos (Media)/`**: `.mp4`, `.avi`, `.mkv`, `.mov`

### 📦 Installation & Setup

#### Prerequisites
Only a standard local installation of Python 3.x is required (Tkinter comes pre-bundled with Python core).

1. Clone the repository or download the script file:
   ```bash
   git clone https://github.comhttps://github.com/KristinaAlokhina/download-organizer
   ```
2. Navigate into the application workspace:
   ```bash
   cd download_organizer
   ```
3. Run the desktop setup:
   ```bash
   Organizer.py
   ```
