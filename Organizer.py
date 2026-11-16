import os
import shutil
import sys
import time
import threading
from datetime import datetime
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog

class DownloadOrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Download Organizer v3.1")
        self.root.geometry("680x480")
        self.root.minsize(550, 380)
        
        # Steuerungsvariablen
        self.is_monitoring = False
        self.target_dir = self.get_default_target_directory()
        self.monitor_thread = None
        
        # Design-Stile konfigurieren
        self.setup_styles()
        # Visuelle Elemente erstellen
        self.create_widgets()
        
        # Begrüßungsnachricht ausgeben
        self.log_info(f"Programm initialisiert. Zielverzeichnis: {self.target_dir}")

    def get_default_target_directory(self):
        """Ermittelt den Pfad zum Download-Ordner des Benutzers."""
        user_profile = os.environ.get("USERPROFILE")
        if not user_profile:
            return os.path.expanduser("~/Downloads")
        return os.path.join(user_profile, "Downloads")

    def setup_styles(self):
        """Konfiguriert moderne Flat-Styles für Buttons und Panels."""
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#f5f6f8')
        style.configure('TLabel', background='#f5f6f8', font=('Segoe UI', 10))
        style.configure('Header.TLabel', font=('Segoe UI', 12, 'bold'))
        style.configure('Status.TLabel', font=('Segoe UI', 10, 'italic'))
        
        # Button-Stile
        style.configure('Action.TButton', font=('Segoe UI', 10, 'bold'), foreground='white', borderwidth=0)
        style.configure('Sort.TButton', background='#2ecc71')
        style.map('Sort.TButton', background=[('active', '#27ae60')])
        style.configure('Start.TButton', background='#3498db')
        style.map('Start.TButton', background=[('active', '#2980b9')])
        style.configure('Stop.TButton', background='#e74c3c')
        style.map('Stop.TButton', background=[('active', '#c0392b')])

    def create_widgets(self):
        """Erstellt das Layout der visuellen Elemente der Anwendung."""
        self.root.configure(background='#f5f6f8')
        
        # Hauptcontainer
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Titel
        header_lbl = ttk.Label(main_frame, text="Download Organizer", style='Header.TLabel')
        header_lbl.pack(anchor=tk.W, pady=(0, 2))
        
        # Pfad-Anzeige & Änderungs-Button
        path_frame = ttk.Frame(main_frame)
        path_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.path_lbl = ttk.Label(path_frame, text=f"Überwachtes Verzeichnis: {self.target_dir}", foreground='#7f8c8d')
        self.path_lbl.pack(side=tk.LEFT, anchor=tk.W)
        
        btn_change_dir = ttk.Button(path_frame, text="📁 Ordner wählen", command=self.change_directory)
        btn_change_dir.pack(side=tk.RIGHT)
        
        # Aktionsleiste mit Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.btn_sort_now = ttk.Button(btn_frame, text="⚡ Jetzt sortieren", style='Sort.TButton', command=self.run_single_sort)
        self.btn_sort_now.pack(side=tk.LEFT, padx=(0, 10))
        
        self.btn_toggle_monitor = ttk.Button(btn_frame, text="🔄 Hintergrundmodus starten", style='Start.TButton', command=self.toggle_monitoring)
        self.btn_toggle_monitor.pack(side=tk.LEFT)
        
        # Statusanzeige
        self.status_lbl = ttk.Label(main_frame, text="Status: Warten auf Benutzeraktion...", style='Status.TLabel', foreground='#555')
        self.status_lbl.pack(anchor=tk.W, pady=(0, 5))
        
        # Log-Konsole (Ausgabefeld für Aktionen)
        self.log_area = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, font=('Consolas', 10), bg='#1e1e1e', fg='#ffffff')
        self.log_area.pack(fill=tk.BOTH, expand=True)
        
        # Tags für die Farbkodierung des Konsolentextes
        self.log_area.tag_config('success', foreground='#2ecc71')
        self.log_area.tag_config('warn', foreground='#f1c40f')
        self.log_area.tag_config('error', foreground='#e74c3c')
        self.log_area.tag_config('info', foreground='#3498db')

    def change_directory(self):
        """Ermöglicht die Auswahl eines benutzerdefinierten Ordners."""
        if self.is_monitoring:
            self.log_warn("Bitte stoppen Sie die Überwachung vor dem Ändern des Ordners.")
            return
        
        new_dir = filedialog.askdirectory(initialdir=self.target_dir, title="Zielverzeichnis auswählen")
        if new_dir:
            self.target_dir = new_dir
            self.path_lbl.config(text=f"Überwachtes Verzeichnis: {self.target_dir}")
            self.log_info(f"Zielverzeichnis geändert zu: {self.target_dir}")

    def append_log(self, prefix, message, tag=None):
        """Fügt eine Zeile sicher in das Textfeld ein."""
        timestamp = datetime.now().strftime('%H:%M:%S')
        self.log_area.insert(tk.END, f"[{timestamp}] {prefix}: {message}\n", tag)
        self.log_area.see(tk.END)

    def log_success(self, msg): self.append_log("✔ ERFOLG", msg, 'success')
    def log_warn(self, msg):    self.append_log("⚠ WARNUNG", msg, 'warn')
    def log_error(self, msg):   self.append_log("✖ FEHLER", msg, 'error')
    def log_info(self, msg):    self.append_log("ℹ INFO", msg, 'info')

    def update_status_safe(self, text):
        """Aktualisiert die Statusleiste threadsicher aus jedem Thread heraus."""
        self.root.after(0, lambda: self.status_lbl.config(text=text))

    def is_file_ready(self, file_path):
        try:
            with open(file_path, 'rb'): 
                return True
        except IOError:
            return False

    def execute_sorting(self, silent_on_empty=False):
        """Hauptfunktion zum Verschieben von Dateien."""
        FILE_TYPES = {
            'Bilder': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'],
            'Dokumente': ['.pdf', '.docx', '.xlsx', '.txt', '.pptx', '.csv'],
            'Skripte': ['.py', '.cs', '.sh', '.bat', '.json', '.html', '.css'],
            'Installer': ['.exe', '.msi', '.zip', '.rar', '.7z'],
            'Musik': ['.mp3', '.wav', '.flac', '.aac'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        }

        if not os.path.exists(self.target_dir):
            self.log_error(f"Zielverzeichnis existiert nicht: {self.target_dir}")
            return 0

        current_script_name = os.path.basename(sys.argv[0]) if sys.argv else ""
        stats = {"erfolgreich": 0, "fehlgeschlagen": 0}
        any_files_found = False

        try:
            entries = list(os.scandir(self.target_dir))
        except Exception as e:
            self.log_error(f"Verzeichnis konnte nicht gelesen werden: {e}")
            return 0

        for entry in entries:
            if not entry.is_file() or entry.name == current_script_name:
                continue

            file_ext = os.path.splitext(entry.name)[1].lower()
            
            for folder_name, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    any_files_found = True
                    
                    if not self.is_file_ready(entry.path):
                        self.log_warn(f"Datei vom System blockiert (wird noch heruntergeladen?): {entry.name}")
                        stats["fehlgeschlagen"] += 1
                        break

                    destination_folder = os.path.join(self.target_dir, folder_name)
                    os.makedirs(destination_folder, exist_ok=True)

                    dest_path = os.path.join(destination_folder, entry.name)
                    
                    # Schutz vor Überschreibung bei gleichem Dateinamen
                    if os.path.exists(dest_path):
                        base, ext = os.path.splitext(entry.name)
                        counter = 1
                        while os.path.exists(dest_path):
                            dest_path = os.path.join(destination_folder, f"{base}_{counter}{ext}")
                            counter += 1

                    try:
                        shutil.move(entry.path, dest_path)
                        new_name = os.path.basename(dest_path)
                        self.log_success(f"Verschoben: {new_name} ➔ {folder_name}/")
                        stats["erfolgreich"] += 1
                    except Exception as e:
                        self.log_error(f"Fehler beim Verschieben von {entry.name}: {e}")
                        stats["fehlgeschlagen"] += 1
                    break

        if not any_files_found and not silent_on_empty:
            self.log_info("Keine neuen Dateien zum Sortieren gefunden.")
            
        return stats["erfolgreich"]

    def run_single_sort(self):
        """Handler für den Button 'Jetzt sortieren'."""
        self.status_lbl.config(text="Status: Einmalige Sortierung wird ausgeführt...")
        self.root.update_idletasks()
        count = self.execute_sorting(silent_on_empty=False)
        if count > 0:
            self.status_lbl.config(text=f"Status: Erfolgreich sortierte Dateien: {count}")
        else:
            self.status_lbl.config(text="Status: Überprüfung abgeschlossen, Ordner leer.")

    def toggle_monitoring(self):
        """Schaltet den Hintergrundmodus um (Start/Stopp)."""
        if not self.is_monitoring:
            self.is_monitoring = True
            self.btn_toggle_monitor.config(text="⏹ Überwachung stoppen", style='Stop.TButton')
            self.btn_sort_now.config(state=tk.DISABLED)
            self.log_info("Hintergrundüberwachung mit einem Intervall von 10 Sekunden gestartet.")
            
            self.monitor_thread = threading.Thread(target=self.monitoring_loop, daemon=True)
            self.monitor_thread.start()
        else:
            self.is_monitoring = False
            self.btn_toggle_monitor.config(text="🔄 Hintergrundmodus starten", style='Start.TButton')
            self.btn_sort_now.config(state=tk.NORMAL)
            self.status_lbl.config(text="Status: Hintergrundüberwachung gestoppt.")
            self.log_info("Hintergrundüberwachung deaktiviert.")

    def monitoring_loop(self):
        """Überwachungsschleife, die im Hintergrund läuft."""
        while self.is_monitoring:
            for _ in range(100):
                if not self.is_monitoring:
                    break
                if _ % 10 == 0:
                    countdown = 10 - (_ // 10)
                    self.update_status_safe(f"Status: Überwachung aktiv (Nächste Prüfung in {countdown} Sek...)")
                time.sleep(0.1)
            
            if not self.is_monitoring:
                break
                
            self.update_status_safe("Status: Ordner wird gescannt...")
            count = self.execute_sorting(silent_on_empty=True)
            if count > 0:
                self.log_info(f"Hintergrundmodus: Automatisch aufgeräumte Dateien: {count}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DownloadOrganizerGUI(root)
    root.mainloop()
    
