# Download Organizer & Automator

<p align="center">
  <a href="#-deutsch">Deutsch</a> • 
  <a href="#-english">English</a>
</p>

---

## 🇩🇪 Deutsch

### 🚀 Funktionen
* **Duale Ausführungsmodi**: Interaktive Auswahl zwischen einer einmaligen Bereinigung oder einer permanenten Hintergrundüberwachung.
* **Permanente Überwachung**: Im Hintergrundmodus überprüft das Skript das Verzeichnis vollautomatisch alle 10 Sekunden auf neue Dateien.
* **Dateizugriffsprüfung**: Verhindert Fehler beim Verschieben, indem aktiv geprüft wird, ob eine Datei noch heruntergeladen oder vom System blockiert wird.
* **Native Windows-Benachrichtigungen**: Nutzt die integrierte Windows-API (`ctypes`), um native Infoboxen direkt im Vordergrund anzuzeigen.
* **Ressourceneffizientes Logging**: Erstellt detaillierte Berichte im System-Home-Verzeichnis, unterdrückt jedoch leere Log-Einträge im Hintergrundmodus.
* **Sicherer Datei-Schutz**: Erkennt dynamisch das aktuell ausgeführte Skript und schützt sich selbst vor unbeabsichtigtem Verschieben.

### 🛠️ Technologien
* Python 3.x
* Integrierte Systemmodule: `os`, `shutil`, `sys`, `time`, `datetime`
* Windows-API Integration: `ctypes` (Keine Installation von Drittanbieter-Paketen erforderlich)

### 📦 Installation & Start
1. Repository klonen:
   ```bash
   git clone https://github.com/KristinaAlokhina/download-organizer
   ```
2. In den Projektordner wechseln:
   ```bash
   cd Organizer
   ```
3. Skript standardmäßig ausführen:
   ```bash
   python Organizer.py
   ```
4. **Tipp (Unsichtbarer Hintergrundmodus):** Benennen Sie die Datei in `Organizer.pyw` um und starten Sie sie. Das Skript läuft komplett ohne Konsolenfenster im Hintergrund.

---

## 🇺🇸 English

### 🚀 Features
* **Dual Execution Modes**: Interactive selection between a single-run optimization and a continuous background monitoring loop.
* **Continuous Directory Watch**: In background mode, the automation script scans the directory autonomously every 10 seconds.
* **File Lock Verification**: Actively checks if a file is still downloading or locked by the system to prevent transfer errors.
* **Native Windows Notifications**: Utilizes the built-in Windows API (`ctypes`) to throw clean, native modal message boxes.
* **Optimized Logging System**: Stores analytical run logs in the user's home path, preventing empty report cluttering when no files are moved.
* **Self-Preservation Guard**: Dynamically resolves the active script name to completely protect itself from being relocated.

### 🛠️ Technologies
* Python 3.x
* Standard core modules: `os`, `shutil`, `sys`, `time`, `datetime`
* Windows-API Integration: `ctypes` (Zero third-party installations needed)

### 📦 Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/KristinaAlokhina/download-organizer
   ```
2. Navigate to the project directory:
   ```bash
   cd Organizer
   ```
3. Run the script normally:
   ```bash
   python Organizer.py
   ```
4. **Tip (Invisible Background Mode):** Rename the file to `Organizer.pyw` and execute it. The script will run completely hidden without opening a console window.
