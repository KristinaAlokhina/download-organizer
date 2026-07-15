import os
import shutil
import sys
from datetime import datetime

def sort_files(target_directory):
    # Identifizierung von Dateikategorien und deren Dateiendungen
    FILE_TYPES = {
        'Bilder': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Dokumente': ['.pdf', '.docx', '.xlsx', '.txt', '.pptx'],
        'Skripte': ['.py', '.cs', '.sh', '.bat'],
        'Installer': ['.exe', '.msi', '.zip', '.rar'],
        'Musik': ['.mp3', '.wav', '.flac', '.aac'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    }

    if not os.path.exists(target_directory):
        print(f"[FEHLER] Das Verzeichnis {target_directory} existiert nicht.")
        return

    # Eigener, sicherer Ordner für Logs außerhalb des Download-Ordners
    user_home = os.path.expanduser("~")
    log_directory = os.path.join(user_home, "Download_Organizer_Logs")
    os.makedirs(log_directory, exist_ok=True)
    log_file_path = os.path.join(log_directory, "sort_report.txt")
    
    # Den Namen des aktuell ausgeführten Skripts ermitteln, um es nicht zu verschieben
    current_script_name = os.path.basename(sys.argv[0]) if sys.argv else ""
    
    # Listen für den Log-Bericht vorbereiten
    log_lines = []
    log_lines.append(f"=== Dateisortierung gestartet ===")
    log_lines.append(f"Zeitpunkt: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_lines.append(f"Zielverzeichnis: {target_directory}")
    log_lines.append("-" * 50)

    # Zähler für die Statistik
    stats = {
        "erfolgreich": 0,
        "fehlgeschlagen": 0,
        "nicht_unterstuetzt": 0
    }

    # Ordner wird durchsucht
    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)

        # Ordner überspringen
        if os.path.isdir(file_path):
            continue
            
        # WICHTIG: Diese auszuführende EXE/Skript komplett ignorieren!
        if filename == current_script_name:
            continue

        # Die Dateiendung bestimmen
        file_ext = os.path.splitext(filename)[1].lower()
        kategorie_gefunden = False

        for folder_name, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                kategorie_gefunden = True
                destination_folder = os.path.join(target_directory, folder_name)
                os.makedirs(destination_folder, exist_ok=True)

                # Verschieben der Datei in die entsprechende Kategorie
                try:
                    shutil.move(file_path, os.path.join(destination_folder, filename))
                    log_lines.append(f"[ERFOLG] {filename} -> {folder_name}/")
                    stats["erfolgreich"] += 1
                except Exception as e:
                    log_lines.append(f"[FEHLER] Konnte {filename} nicht verschieben: {e}")
                    stats["fehlgeschlagen"] += 1
                break
        
        if not kategorie_gefunden:
            stats["nicht_unterstuetzt"] += 1

    # Abschlussbericht und Statusprüfung für den Log
    log_lines.append("-" * 50)
    log_lines.append("=== BEREINIGUNG ABGESCHLOSSEN ===")
    log_lines.append(f"  Erfolgreich sortiert:  {stats['erfolgreich']}")
    log_lines.append(f"  Nicht unterstützt:     {stats['nicht_unterstuetzt']}")
    log_lines.append(f"  Fehlgeschlagen:        {stats['fehlgeschlagen']}")
    log_lines.append("-" * 50)
    
    if stats["fehlgeschlagen"] == 0:
        log_lines.append("[STATUS] Alles bereit! Der Prozess wurde erfolgreich und ohne Fehler beendet.")
    else:
        log_lines.append("[STATUS] Prozess beendet, jedoch traten einige Fehler auf.")
    log_lines.append("=" * 50 + "\n")

    # Schreiben aller Daten in die Log-Datei
    try:
        with open(log_file_path, "a", encoding="utf-8") as log_file:
            log_file.write("\n".join(log_lines) + "\n")
    except Exception as e:
        print(f"Fehler beim Schreiben der Log-Datei: {e}")


if __name__ == "__main__":
    user_profile = os.environ.get("USERPROFILE")
    if user_profile:
        TARGET = os.path.join(user_profile, "Downloads")
        sort_files(TARGET)
