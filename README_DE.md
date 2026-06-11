Ein automatisiertes Python-Skript zur Bereinigung und Strukturierung des Download-Ordners unter Windows. 

## 🚀 Funktionen
- Automatische Sortierung: Scannt den Download-Ordner und sortiert Dateien nach Typen (Bilder, Dokumente, Skripte, Installer).
- Dynamic Path Detection: Erkennt automatisch den Pfad des aktuellen Windows-Benutzers über Systemvariablen (`USERPROFILE`).
- Standalone App: Kann mit PyInstaller in eine eigenständige `.exe`-Datei ohne Python-Abhängigkeiten kompiliert werden.

## 🛠️ Technologien
- Python 3.10+
- Integrierte Module: `os`, `shutil`, `sys`
- Externe Bibliotheken: `PyInstaller` (für den Build-Prozess)

## 📦 Installation & Start
1. Repository klonen: 
	git clone https://github.com/KristinaAlokhina/download-organizer.git
2. Skript ausführen: 
	python organizer.py

Alternativ kann das Skript als ausführbare Datei kompiliert werden:

python -m PyInstaller --onefile --noconsole organizer.py