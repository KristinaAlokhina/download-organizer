# Download Organizer & Automator

<p align="center">
  <a href="#-deutsch">Deutsch</a> • 
  <a href="#-english">English</a>
</p>

---

## 🇩🇪 Deutsch

### 🚀 Funktionen
* **Duale Ausführungsmodi**: Der Benutzer kann interaktiv zwischen einer einmaligen Bereinigung oder einer permanenten Hintergrundüberwachung wählen.
* **Permanente Überwachung**: Im Hintergrundmodus überprüft das Skript das Verzeichnis vollautomatisch alle 10 Sekunden auf neue Dateien.
* **Native Windows-Benachrichtigungen**: Nutzt die integrierte Windows-API (`ctypes`), um nach erfolgreicher Sortierung native Infoboxen direkt im Vordergrund anzuzeigen.
* **Ressourceneffizientes Logging**: Erstellt detaillierte Berichte im System-Home-Verzeichnis, unterdrückt jedoch leere Log-Einträge im Hintergrundmodus, um Speicherplatz zu sparen.
* **Sicherer Datei-Schutz**: Erkennt dynamisch das aktuell ausgeführte Skript oder die kompilierte Anwendung und schützt sich selbst vor unbeabsichtigtem Verschieben.

### 🛠️ Technologien
* Python 3.x
* Integrierte Systemmodule: `os`, `shutil`, `sys`, `time`, `datetime`
* Windows-API Integration: `ctypes` (Keine Installation von Drittanbieter-Paketen erforderlich)

### 📦 Installation & Start
1. Repository klonen:
   ```bash
   git clone https://[github.com](https://github.com/KristinaAlokhina/download-organizer)
   ```
2. In den Projektordner wechseln:
   ```bash
   cd Organizer
   ```
3. Skript ausführen:
   ```bash
   python Organizer.py
   ```

---

## 🇺🇸 English

### 🚀 Features
* **Dual Execution Modes**: Interactive selection between a single-run optimization and a continuous background monitoring loop.
* **Continuous Directory Watch**: In background mode, the automation script scans the directory autonomously every 10 seconds.
* **Native Windows Notifications**: Utilizes the built-in Windows API (`ctypes`) to throw clean, native modal message boxes upon completing actions.
* **Optimized Logging System**: Stores analytical run logs in the user's home path, preventing empty report cluttering when no files are moved.
* **Self-Preservation Guard**: Dynamically resolves the active script name or packaged runtime environment to completely protect itself from being relocated.

### 🛠️ Technologies
* Python 3.x
* Standard core modules: `os`, `shutil`, `sys`, `time`, `datetime`
* Windows-API Integration: `ctypes` (Zero third-party installations needed)

### 📦 Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://[github.com](https://github.com/KristinaAlokhina/download-organizer)
   ```
2. Navigate to the project directory:
   ```bash
   cd Organizer
   ```
3. Run the script:
   ```bash
   python Organizer.py
   ```
