import os
import shutil
import sys
import time
import ctypes
from datetime import datetime

# Windows API Konstanten für MessageBox
MB_OK = 0x00000000
MB_YESNOCANCEL = 0x00000003
MB_ICONINFORMATION = 0x00000040
MB_ICONERROR = 0x00000010
MB_SETFOREGROUND = 0x00010000

# Rückgabewerte für MessageBox
IDYES = 6
IDNO = 7
IDCANCEL = 2

def show_notification(title, message, is_error=False):
    """Zeigt eine native Windows-MessageBox im Vordergrund an."""
    icon = MB_ICONERROR if is_error else MB_ICONINFORMATION
    ctypes.windll.user32.MessageBoxW(0, message, title, MB_OK | icon | MB_SETFOREGROUND)

def sort_files(target_directory):
    FILE_TYPES = {
        'Bilder': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Dokumente': ['.pdf', '.docx', '.xlsx', '.txt', '.pptx'],
        'Skripte': ['.py', '.cs', '.sh', '.bat'],
        'Installer': ['.exe', '.msi', '.zip', '.rar'],
        'Musik': ['.mp3', '.wav', '.flac', '.aac'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    }

    if not os.path.exists(target_directory):
        return False

    user_home = os.path.expanduser("~")
    log_directory = os.path.join(user_home, "Download_Organizer_Logs")
    os.makedirs(log_directory, exist_ok=True)
    log_file_path = os.path.join(log_directory, "sort_report.txt")
    
    current_script_name = os.path.basename(sys.argv[0]) if sys.argv else ""
    
    log_lines = []
    log_lines.append("=== Dateisortierung gestartet ===")
    log_lines.append(f"Zeitpunkt: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_lines.append(f"Zielverzeichnis: {target_directory}")
    log_lines.append("-" * 50)

    stats = {"erfolgreich": 0, "fehlgeschlagen": 0, "nicht_unterstuetzt": 0}
    any_files_processed = False

    try:
        files = os.listdir(target_directory)
    except Exception:
        return False

    for filename in files:
        file_path = os.path.join(target_directory, filename)

        if os.path.isdir(file_path):
            continue
            
        if filename == current_script_name:
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        kategorie_gefunden = False

        for folder_name, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                kategorie_gefunden = True
                any_files_processed = True
                destination_folder = os.path.join(target_directory, folder_name)
                os.makedirs(destination_folder, exist_ok=True)

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

    if not any_files_processed:
        return False

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

    try:
        with open(log_file_path, "a", encoding="utf-8") as log_file:
            log_file.write("\n".join(log_lines) + "\n")
    except Exception:
        pass
        
    return stats["erfolgreich"]

if __name__ == "__main__":
    user_profile = os.environ.get("USERPROFILE")
    if not user_profile:
        show_notification("Download Organizer", "Fehler: USERPROFILE-Umgebungsvariable nicht gefunden.", is_error=True)
        sys.exit(1)
        
    TARGET = os.path.join(user_profile, "Downloads")

    dialog_text = (
        "Wählen Sie den Ausführungsmodus für Download Organizer:\n\n"
        "[JA] - Einmalige Ausführung (Jetzt sortieren)\n"
        "[NEIN] - Permanenter Hintergrundmodus (Ordner kontinuierlich überwachen)\n"
        "[ABBRECHEN] - Programm beenden"
    )
    
    res = ctypes.windll.user32.MessageBoxW(
        0, dialog_text, "Download Organizer - Modusauswahl", 
        MB_YESNOCANCEL | MB_ICONINFORMATION | MB_SETFOREGROUND
    )

    if res == IDYES:
        anzahl = sort_files(TARGET)
        if anzahl and anzahl > 0:
            show_notification("Download Organizer", f"Sortierung abgeschlossen!\n{anzahl} Dateien erfolgreich sortiert.")
        else:
            show_notification("Download Organizer", "Sortierung abgeschlossen! Keine neuen Dateien zum Sortieren gefunden.")
            
    elif res == IDNO:
        show_notification("Download Organizer", "Hintergrundüberwachung wurde erfolgreich gestartet!\nDas Programm läuft nun unsichtbar im Hintergrund.")
        
        while True:
            anzahl = sort_files(TARGET)
            if anzahl and anzahl > 0:
                show_notification("Download Organizer (Hintergrund)", f"{anzahl} neue Dateien wurden automatisch sortiert.")
            time.sleep(10)
            
    else:
        sys.exit(0)
