import os
import shutil
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
        print(f"Fehler: Das Verzeichnis {target_directory} existiert nicht.")
        return


    print(f"Starte Bereinigung im Verzeichnis: {target_directory}")
    files_moved = 0

    # Ordner wird durchsucht
    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)

        # Ordner überspringen
        if os.path.isdir(file_path):
            continue

        # Die Dateiendung bestimmen
        file_ext = os.path.splitext(filename)[1].lower()


        for folder_name, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                # Erstellen Sie einen Ordner für die Kategorie, falls dieser noch nicht existiert.
                destination_folder = os.path.join(target_directory, folder_name)
                os.makedirs(destination_folder, exist_ok=True)

                # Verschieben der Datei in die entsprechende Kategorie
                try:
                    shutil.move(file_path, os.path.join(destination_folder, filename))
                    print(f"[ERFOLG] {filename} -> {folder_name}/")
                    files_moved += 1
                except Exception as e:
                    print(f"[FEHLER] Konnte {filename} nicht verschieben: {e}")
                break

    print(f"Bereinigung abgeschlossen. {files_moved} Dateien wurden sortiert.")


if __name__ == "__main__":
    import os
    
    # Automatisch den Pfad zum „Downloads“-Ordner des aktuellen Windows-Benutzers ermitteln
    user_profile = os.environ.get("USERPROFILE")
    TARGET = os.path.join(user_profile, "Downloads")
    
    # Beginn der Sortierung der eigentlichen Dateien im Download-Ordner
    sort_files(TARGET)