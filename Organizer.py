import os
import shutil
import sys
import time
import ctypes
from datetime import datetime

# Windows-API-Konstanten fuer die Anzeige von MessageBoxen
MB_OK = 0x00000000
MB_YESNOCANCEL = 0x00000003
MB_ICONINFORMATION = 0x00000040
MB_ICONERROR = 0x00000010
MB_SETFOREGROUND = 0x00010000

# Rueckgabewerte der Windows-MessageBox zur Erkennung des gedrueckten Buttons
IDYES = 6
IDNO = 7
IDCANCEL = 2

def show_notification(title, message, is_error=False):
    """Zeigt eine native Windows-MessageBox im Vordergrund an."""
    # Bestimmung des Icons basierend auf dem Fehlertyp
    icon = MB_ICONERROR if is_error else MB_ICONINFORMATION
    # Aufruf der Windows-API-Funktion fuer das native Dialogfenster
    ctypes.windll.user32.MessageBoxW(0, message, title, MB_OK | icon | MB_SETFOREGROUND)

def is_file_ready(file_path):
    """Prueft, ob die Datei vollstaendig geschrieben wurde und nicht blockiert ist."""
    try:
        # Versucht die Datei im Binarmodus zu oeffnen, um den Zugriff zu testen
        with open(file_path, 'rb'):
            return True
    except IOError:
        # Wenn der Zugriff verweigert wird, wird die Datei noch vom System blockiert
        return False

def sort_files(target_directory):
    # Definition der Zielordner und den dazugehoerigen Dateiendungen
    FILE_TYPES = {
        'Bilder': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Dokumente': ['.pdf', '.docx', '.xlsx', '.txt', '.pptx'],
        'Skripte': ['.py', '.cs', '.sh', '.bat'],
        'Installer': ['.exe', '.msi', '.zip', '.rar'],
        'Musik': ['.mp3', '.wav', '.flac', '.aac'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    }

    # Pruefung, ob das angegebene Zielverzeichnis existiert
    if not os.path.exists(target_directory):
        return False

    # Pfad fuer den Log-Ordner im Benutzerverzeichnis ermitteln und erstellen
    user_home = os.path.expanduser("~")
    log_directory = os.path.join(user_home, "Download_Organizer_Logs")
    os.makedirs(log_directory, exist_ok=True)
    log_file_path = os.path.join(log_directory, "sort_report.txt")
    
    # Namen des aktuell laufenden Skripts ermitteln, um Selbstverschiebung zu verhindern
    current_script_name = os.path.basename(sys.argv[0]) if sys.argv else ""
    
    # Vorbereitung des Log-Headers fuer diesen Sortierdurchlauf
    log_lines = []
    log_lines.append("=== Dateisortierung gestartet ===")
    log_lines.append(f"Zeitpunkt: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_lines.append(f"Zielverzeichnis: {target_directory}")
    log_lines.append("-" * 50)

    # Initialisierung der Zaehler fuer die Statistik
    stats = {"erfolgreich": 0, "fehlgeschlagen": 0, "nicht_unterstuetzt": 0}
    any_files_processed = False

    try:
        # Optimiertes Einlesen des Verzeichnisses mittels os.scandir fuer bessere Performance
        entries = list(os.scandir(target_directory))
    except Exception:
        return False

    # Iteration durch alle gefundenen Eintraege im Verzeichnis
    for entry in entries:
        # Ordner werden bei der Verarbeitung uebersprungen
        if not entry.is_file():
            continue
            
        # Das eigene Skript wird nicht verschoben
        if entry.name == current_script_name:
            continue

        # Extraktion und Normalisierung der Dateiendung zur Kategorisierung
        file_ext = os.path.splitext(entry.name)[1].lower()
        kategorie_gefunden = False

        # Abgleich der Dateiendung mit den definierten Kategorien
        for folder_name, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                kategorie_gefunden = True
                any_files_processed = True
                
                # Pruefung, ob die Datei bereit ist oder noch heruntergeladen wird
                if not is_file_ready(entry.path):
                    log_lines.append(f"[GEBLOCKT] {entry.name} wird noch verwendet.")
                    stats["fehlgeschlagen"] += 1
                    break

                # Erstellung des Zielordners, falls dieser noch nicht existiert
                destination_folder = os.path.join(target_directory, folder_name)
                os.makedirs(destination_folder, exist_ok=True)

                try:
                    # Verschieben der Datei in den entsprechenden Kategorieordner
                    shutil.move(entry.path, os.path.join(destination_folder, entry.name))
                    log_lines.append(f"[ERFOLG] {entry.name} -> {folder_name}/")
                    stats["erfolgreich"] += 1
                except Exception as e:
                    # Protokollierung von Fehlern, falls das Verschieben fehlschlagt
                    log_lines.append(f"[FEHLER] Konnte {entry.name} nicht verschieben: {e}")
                    stats["fehlgeschlagen"] += 1
                break
        
        # Zaehler erhoehen, wenn die Dateiendung in keiner Kategorie definiert ist
        if not kategorie_gefunden:
            stats["nicht_unterstuetzt"] += 1

    # Wenn keine relevanten Dateien gefunden wurden, wird der Vorgang abgebrochen
    if not any_files_processed:
        return False

    # Zusammenfassung des Berichts fuer die Logdatei erstellen
    log_lines.append("-" * 50)
    log_lines.append("=== BEREINIGUNG ABGESCHLOSSEN ===")
    log_lines.append(f"  Erfolgreich sortiert:  {stats['erfolgreich']}")
    log_lines.append(f"  Nicht unterstützt:     {stats['nicht_unterstuetzt']}")
    log_lines.append(f"  Fehlgeschlagen:        {stats['fehlgeschlagen']}")
    log_lines.append("-" * 50)
    
    # Statusmeldung basierend auf dem Erfolg der Operationen festlegen
    if stats["fehlgeschlagen"] == 0:
        log_lines.append("[STATUS] Alles bereit! Der Prozess wurde erfolgreich und ohne Fehler beendet.")
    else:
        log_lines.append("[STATUS] Prozess beendet, jedoch traten einige Fehler auf.")
    log_lines.append("=" * 50 + "\n")

    try:
        # Schreiben der gesammelten Log-Zeilen in die Textdatei
        with open(log_file_path, "a", encoding="utf-8") as log_file:
            log_file.write("\n".join(log_lines) + "\n")
    except Exception:
        pass
        
    return stats["erfolgreich"]

if __name__ == "__main__":
    # Abfragen der Windows-Umgebungsvariable fuer das Benutzerprofil
    user_profile = os.environ.get("USERPROFILE")
    if not user_profile:
        show_notification("Download Organizer", "Fehler: USERPROFILE-Umgebungsvariable nicht gefunden.", is_error=True)
        sys.exit(1)
        
    # Pfad zum Standard-Download-Ordner des Benutzers definieren
    TARGET = os.path.join(user_profile, "Downloads")

    # Vorbereitung des Textes fuer das Modusauswahl-Fenster
    dialog_text = (
        "Wählen Sie den Ausführungsmodus für Download Organizer:\n\n"
        "[JA] - Einmalige Ausführung (Jetzt sortieren)\n"
        "[NEIN] - Permanenter Hintergrundmodus (Ordner kontinuierlich überwachen)\n"
        "[ABBRECHEN] - Programm beenden"
    )
    
    # Anzeige der Modusauswahl beim Start des Programms
    res = ctypes.windll.user32.MessageBoxW(
        0, dialog_text, "Download Organizer - Modusauswahl", 
        MB_YESNOCANCEL | MB_ICONINFORMATION | MB_SETFOREGROUND
    )

    # Logik fuer die einmalige Ausfuehrung (Button JA)
    if res == IDYES:
        anzahl = sort_files(TARGET)
        if anzahl and anzahl > 0:
            show_notification("Download Organizer", f"Sortierung abgeschlossen!\n{anzahl} Dateien erfolgreich sortiert.")
        else:
            show_notification("Download Organizer", "Sortierung abgeschlossen! Keine neuen Dateien zum Sortieren gefunden.")
            
    # Logik fuer den permanenten Hintergrundmodus (Button NEIN)
    elif res == IDNO:
        show_notification("Download Organizer", "Hintergrundüberwachung wurde erfolgreich gestartet!\nDas Programm läuft nun unsichtbar im Hintergrund.")
        
        # Endlosschleife fuer die kontinuierliche Ueberwachung im Hintergrund
        while True:
            # Sortierung ausfuehren; Benachrichtigungen im Loop unterdrueckt, um Blockaden zu vermeiden
            sort_files(TARGET)
            # 10 Sekunden Pause vor dem naechsten Pruefdurchlauf
            time.sleep(10)
            
    # Programm beenden, wenn Abbrechen oder Schliessen gewaehlt wurde
    else:
        sys.exit(0)
