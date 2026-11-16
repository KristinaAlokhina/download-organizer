&#x20;\<p align="center">   \<ins>\<b>\<kbd>&nbsp;DESKTOP APPLICATION · v3.1.0&nbsp;\</kbd>\</b>\</ins> \</p>

\<h1 align="center">   🎯 DOWNLOAD ORGANIZER \</h1>

\<p align="center">   \<strong>A smarter way to organize your downloads.\</strong>   \<br>   \<i>A lightweight desktop application built with Python and Tkinter, featuring automated file sorting, background monitoring, and a clean graphical interface.\</i> \</p>

\<p align="center">   \<a href="#-deutsch">🇩🇪 Deutsch\</a> •   \<a href="#-english">🇺🇸 English\</a> •   \<a href="#-русский">🇷🇺 Русский\</a> •   \<a href="#-українська">🇺🇦 Українська\</a> \</p>

\<p align="center">   \<kbd>Python\</kbd>   \<kbd>Tkinter\</kbd>   \<kbd>Multithreading\</kbd>   \<kbd>Windows\</kbd> \</p>


---

## 🇩🇪 Deutsch

**Download Organizer** ist eine Desktop-Anwendung zur automatischen Organisation von Dateien. Sie überwacht einen ausgewählten Ordner im Hintergrund und sortiert heruntergeladene Dateien anhand ihrer Dateiendungen in übersichtliche Unterordner.

Die Anwendung verfügt über eine moderne grafische Benutzeroberfläche (GUI), eine integrierte Protokollkonsole und verschiedene Funktionen zum Schutz vorhandener Dateien.

### 🚀 Funktionen

- **Modernes Flat-UI-Design 🎨:** Eine übersichtliche grafische Benutzeroberfläche mit farblich abgestimmten Schaltflächen und intuitiver Navigation.
- **Echtzeit-Protokollkonsole 📝:** Zeigt Dateiaktionen und Systemmeldungen direkt in der Anwendung an. Unterschiedliche Meldungstypen werden farblich hervorgehoben (Info, Erfolg, Warnung und Fehler).
- **Automatische Hintergrundüberwachung 🔄:** Überwacht das ausgewählte Verzeichnis in regelmäßigen Abständen (alle 10 Sekunden), ohne die Benutzeroberfläche zu blockieren.
- **Dateischutz 🔒:** Erkennt, ob eine Datei noch verwendet oder geschrieben wird, und vermeidet vorzeitige Verschiebungen.
- **Individuelle Ordnerauswahl 📁:** Ermöglicht die Auswahl und Änderung des zu überwachenden Verzeichnisses direkt über die GUI.
- **Überschreibschutz 🛡️:** Verhindert das Überschreiben gleichnamiger Dateien durch die automatische Vergabe eindeutiger Dateinamen.
- **Verbesserte Thread-Sicherheit ⚙️:** Verwendet sichere asynchrone Mechanismen für die Kommunikation zwischen Hintergrundprozessen und Benutzeroberfläche.
- **Selbst-Ausschluss:** Erkennt die eigene Anwendungsdatei und verhindert, dass sie versehentlich mitorganisiert wird.

### 🛠️ Verwendete Technologien

| Technologie   | Verwendung                                        |
| ------------- | ------------------------------------------------- |
| Python 3.x    | Programmiersprache                                |
| Tkinter / ttk | Grafische Benutzeroberfläche                      |
| `threading`   | Hintergrundüberwachung und parallele Verarbeitung |
| `os.scandir`  | Effizientes Durchsuchen von Verzeichnissen        |
| `shutil`      | Dateioperationen und Verschiebungen               |
| `os`          | Dateisystemverwaltung                             |

### 📂 Unterstützte Dateitypen

Dateien werden anhand ihrer Dateiendungen automatisch den folgenden Kategorien zugeordnet:

| Zielordner   | Unterstützte Formate                                  |
| ------------ | ----------------------------------------------------- |
| `Bilder/`    | `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.webp`      |
| `Dokumente/` | `.pdf`, `.docx`, `.xlsx`, `.txt`, `.pptx`, `.csv`     |
| `Skripte/`   | `.py`, `.cs`, `.sh`, `.bat`, `.json`, `.html`, `.css` |
| `Installer/` | `.exe`, `.msi`, `.zip`, `.rar`, `.7z`                 |
| `Musik/`     | `.mp3`, `.wav`, `.flac`, `.aac`                       |
| `Videos/`    | `.mp4`, `.avi`, `.mkv`, `.mov`                        |

### 📦 Installation & Ausführung

#### Voraussetzungen

- Python 3.x (für die Ausführung aus dem Quellcode)
- Windows (für die bereitgestellte `.exe`-Version)

#### 🔹 Option 1: Standalone-Version (Empfohlen)

1. Lade `DownloadOrganizer.zip` aus dem Bereich **Releases → Assets** herunter.
2. Entpacke das ZIP-Archiv.
3. Starte `DownloadOrganizer.exe`.

**Keine separate Python-Installation erforderlich!**

#### 🔹 Option 2: Aus dem Quellcode starten

1. Repository klonen:

```bash
git clone https://github.com/KristinaAlokhina/download-organizer.git
```

2. In das Projektverzeichnis wechseln:

```bash
cd download-organizer
```

3. Anwendung starten:

```bash
python Organizer.py
```

---

## 🇺🇸 English

**Download Organizer** is a desktop application designed to automatically organize files. It monitors a selected directory in the background and sorts downloaded files into dedicated subfolders based on their file extensions.

The application features a modern graphical user interface (GUI), an integrated logging console, and several mechanisms designed to protect existing files.

### 🚀 Features

- **Modern Flat UI Design 🎨:** A clean graphical interface featuring color-coded buttons and intuitive navigation.
- **Real-time Log Console 📝:** Displays file operations and application events directly within the interface. Different message types are visually distinguished (Info, Success, Warning, and Error).
- **Automatic Background Monitoring 🔄:** Monitors the selected directory at regular intervals (every 10 seconds) without blocking the user interface.
- **File-Lock Protection 🔒:** Detects whether a file is still being accessed or written to, helping prevent premature file transfers.
- **Custom Folder Selection 📁:** Select or change the directory being monitored directly through the GUI.
- **Overwrite Protection 🛡️:** Prevents existing files from being overwritten by automatically generating unique filenames.
- **Improved Thread Safety ⚙️:** Uses safe asynchronous mechanisms for communication between background processes and the user interface.
- **Self-Exclusion:** Recognizes its own application file to prevent accidental file organization.

### 🛠️ Technologies Used

| Technology    | Purpose                                         |
| ------------- | ----------------------------------------------- |
| Python 3.x    | Programming language                            |
| Tkinter / ttk | Graphical user interface                        |
| `threading`   | Background monitoring and concurrent processing |
| `os.scandir`  | Efficient directory scanning                    |
| `shutil`      | File operations and file transfers              |
| `os`          | File system management                          |

### 📂 Supported File Types

Files are automatically categorized into the following directories based on their extensions:

| Destination Folder | Supported Formats                                     |
| ------------------ | ----------------------------------------------------- |
| `Bilder/`          | `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.webp`      |
| `Dokumente/`       | `.pdf`, `.docx`, `.xlsx`, `.txt`, `.pptx`, `.csv`     |
| `Skripte/`         | `.py`, `.cs`, `.sh`, `.bat`, `.json`, `.html`, `.css` |
| `Installer/`       | `.exe`, `.msi`, `.zip`, `.rar`, `.7z`                 |
| `Musik/`           | `.mp3`, `.wav`, `.flac`, `.aac`                       |
| `Videos/`          | `.mp4`, `.avi`, `.mkv`, `.mov`                        |

### 📦 Installation & Setup

#### Requirements

- Python 3.x (for running from source)
- Windows (for the provided standalone `.exe` version)

#### 🔹 Option 1: Standalone Version (Recommended)

1. Download `DownloadOrganizer.zip` from **Releases → Assets**.
2. Extract the ZIP archive.
3. Launch `DownloadOrganizer.exe`.

**No separate Python installation required!**

#### 🔹 Option 2: Run from Source

1. Clone the repository:

```bash
git clone https://github.com/KristinaAlokhina/download-organizer.git
```

2. Navigate to the project directory:

```bash
cd download-organizer
```

3. Launch the application:

```bash
python Organizer.py
```

---

## 🇷🇺 Русский

**Download Organizer** — это настольное приложение для автоматической организации файлов. Оно отслеживает выбранную директорию в фоновом режиме и распределяет загруженные файлы по отдельным папкам в зависимости от их расширений.

Приложение оснащено современным графическим интерфейсом (GUI), встроенной консолью событий и механизмами защиты существующих файлов.

### 🚀 Возможности

- **Современный Flat UI 🎨:** Удобный графический интерфейс с цветными кнопками и понятной навигацией.
- **Консоль событий в реальном времени 📝:** Отображает операции с файлами и системные сообщения непосредственно в приложении. Разные типы сообщений выделяются цветом (Информация, Успех, Предупреждение и Ошибка).
- **Автоматический фоновый мониторинг 🔄:** Проверяет выбранную директорию через определённые промежутки времени (каждые 10 секунд), не блокируя интерфейс.
- **Защита от перемещения занятых файлов 🔒:** Определяет, используется ли файл или продолжается ли его запись, чтобы избежать преждевременного перемещения.
- **Выбор папки 📁:** Позволяет выбирать и менять отслеживаемую директорию непосредственно через графический интерфейс.
- **Защита от перезаписи 🛡️:** Предотвращает перезапись существующих файлов благодаря автоматическому созданию уникальных имён.
- **Улучшенная потокобезопасность ⚙️:** Использует безопасные асинхронные механизмы взаимодействия между фоновыми процессами и интерфейсом.
- **Исключение собственного файла:** Распознаёт собственный исполняемый файл и не допускает его случайной сортировки.

### 🛠️ Используемые технологии

| Технология    | Назначение                           |
| ------------- | ------------------------------------ |
| Python 3.x    | Язык программирования                |
| Tkinter / ttk | Графический интерфейс                |
| `threading`   | Фоновый мониторинг и многопоточность |
| `os.scandir`  | Эффективное сканирование директорий  |
| `shutil`      | Операции с файлами и их перемещение  |
| `os`          | Работа с файловой системой           |

### 📂 Поддерживаемые типы файлов

Файлы автоматически распределяются по следующим категориям на основе их расширений:

| Папка назначения | Поддерживаемые форматы                                |
| ---------------- | ----------------------------------------------------- |
| `Bilder/`        | `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.webp`      |
| `Dokumente/`     | `.pdf`, `.docx`, `.xlsx`, `.txt`, `.pptx`, `.csv`     |
| `Skripte/`       | `.py`, `.cs`, `.sh`, `.bat`, `.json`, `.html`, `.css` |
| `Installer/`     | `.exe`, `.msi`, `.zip`, `.rar`, `.7z`                 |
| `Musik/`         | `.mp3`, `.wav`, `.flac`, `.aac`                       |
| `Videos/`        | `.mp4`, `.avi`, `.mkv`, `.mov`                        |

### 📦 Установка и запуск

#### Требования

- Python 3.x (для запуска из исходного кода).
- Windows (для готовой версии `.exe`).

#### 🔹 Вариант 1: Standalone-версия (Рекомендуется)

1. Скачайте `DownloadOrganizer.zip` из раздела **Releases → Assets**.
2. Распакуйте ZIP-архив.
3. Запустите `DownloadOrganizer.exe`.

**Отдельная установка Python не требуется!**

#### 🔹 Вариант 2: Запуск из исходного кода

1. Клонируйте репозиторий:

```bash
git clone https://github.com/KristinaAlokhina/download-organizer.git
```

2. Перейдите в папку проекта:

```bash
cd download-organizer
```

3. Запустите приложение:

```bash
python Organizer.py
```

---

## 🇺🇦 Українська

**Download Organizer** — це настільний застосунок для автоматичної організації файлів. Він відстежує вибрану директорію у фоновому режимі та розподіляє завантажені файли за окремими папками залежно від їхніх розширень.

Застосунок має сучасний графічний інтерфейс (GUI), вбудовану консоль подій і механізми захисту наявних файлів.

### 🚀 Можливості

- **Сучасний Flat UI 🎨:** Зручний графічний інтерфейс із кольоровими кнопками та зрозумілою навігацією.
- **Консоль подій у реальному часі 📝:** Відображає операції з файлами та системні повідомлення безпосередньо в застосунку. Різні типи повідомлень виділяються кольорами (Інформація, Успіх, Попередження та Помилка).
- **Автоматичний фоновий моніторинг 🔄:** Перевіряє вибрану директорію через певні проміжки часу (кожні 10 секунд), не блокуючи інтерфейс.
- **Захист від переміщення зайнятих файлів 🔒:** Визначає, чи використовується файл або чи триває його запис, щоб уникнути передчасного переміщення.
- **Вибір папки 📁:** Дозволяє вибирати та змінювати директорію моніторингу безпосередньо через графічний інтерфейс.
- **Захист від перезапису 🛡️:** Запобігає перезапису наявних файлів завдяки автоматичному створенню унікальних назв.
- **Покращена потокобезпека ⚙️:** Використовує безпечні асинхронні механізми взаємодії між фоновими процесами та інтерфейсом.
- **Виключення власного файлу:** Розпізнає власний виконуваний файл і запобігає його випадковому сортуванню.

### 🛠️ Використані технології

| Технологія    | Призначення                            |
| ------------- | -------------------------------------- |
| Python 3.x    | Мова програмування                     |
| Tkinter / ttk | Графічний інтерфейс                    |
| `threading`   | Фоновий моніторинг і багатопотоковість |
| `os.scandir`  | Ефективне сканування директорій        |
| `shutil`      | Операції з файлами та їх переміщення   |
| `os`          | Робота з файловою системою             |

### 📂 Підтримувані типи файлів

Файли автоматично розподіляються за такими категоріями на основі їхніх розширень:

| Папка призначення | Підтримувані формати                                  |
| ----------------- | ----------------------------------------------------- |
| `Bilder/`         | `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.webp`      |
| `Dokumente/`      | `.pdf`, `.docx`, `.xlsx`, `.txt`, `.pptx`, `.csv`     |
| `Skripte/`        | `.py`, `.cs`, `.sh`, `.bat`, `.json`, `.html`, `.css` |
| `Installer/`      | `.exe`, `.msi`, `.zip`, `.rar`, `.7z`                 |
| `Musik/`          | `.mp3`, `.wav`, `.flac`, `.aac`                       |
| `Videos/`         | `.mp4`, `.avi`, `.mkv`, `.mov`                        |

### 📦 Встановлення та запуск

#### Вимоги

- Python 3.x (для запуску з вихідного коду).
- Windows (для готової версії `.exe`).

#### 🔹 Варіант 1: Standalone-версія (Рекомендовано)

1. Завантажте `DownloadOrganizer.zip` із розділу **Releases → Assets**.
2. Розпакуйте ZIP-архів.
3. Запустіть `DownloadOrganizer.exe`.

**Окреме встановлення Python не потрібне!**

#### 🔹 Варіант 2: Запуск із вихідного коду

1. Клонуйте репозиторій:

```bash
git clone https://github.com/KristinaAlokhina/download-organizer.git
```

2. Перейдіть до папки проєкту:

```bash
cd download-organizer
```

3. Запустіть застосунок:

```bash
python Organizer.py
```

---

\<p align="center">   \<strong>🎯 Download Organizer\</strong>   \<br />   \<sub>Keep your files organized. Keep your workspace clean.\</sub>   \<br />   \<br />   \<kbd>Made with Python ❤️\</kbd> \</p>
