# Teamplanner

Übung zum Start in Python. Mit dem Somersemester 2022 habe ich mich das erste Mal an Python gesetzt.
Nach einigen Umwegen über Tkinter habe ich das Projekt erst in PyQt5 und nun auf PyQt6.3 angelegt.

### Logging
Um Informationen über den Zustand des Programms zu erhalten werden Informationen in einer Datei geloggt.
Logs werden in der teamplanner.log gespeichert.

### Configparser
Ziel ist die vollständige Konfigurierbarkeit in einer externen Datei aufzubewahren.
Angaben werden momentan in der config.ini gespeichert.

### SQLite3 (In Vorbereitung)
Informationen über Nutzer sollen in einer lokalen Datenbank "db.sqlite" hinterlegt werden.
Vorbereitungen dafür finden sich in der overview.py

### Ctypes
Um in Windows das Fenster-Icon auch in der Taskbar anzeigen zu können, musste ein Identifier in der main.py gesetzt werden.

### Stylesheet
PySide6 (Qt für Python) unterstützt externe Stylesheets, welche nahezu wie CSS aufgebaut sind.
Unter "/assets/themes/stylesheet.qss" werden verschiedene Module visuell angepasst.
Properties werden per TAG[Property] angesteuert; Objektnamen mit TAG#name.

## Viele Bereiche sind noch in Vorbereitung!
/classes/core/project.py ist beispielsweise eine solche Datei. Klasse angelegt, schon erste Tests bzgl. Dialogfenster zur Dateienauswahl abgeschlossen. Aber noch vieles zu erledigen.

## Status
Momentan kann das Programm geöffnet und genutzt werden, (noch) vordefinierte Einträge werden durch die Klasse "Person" angelegt. Man kann ihre Fähigkeiten togglen und der Icon-Text der PushButton werden je nach Kategorie eingefärbt.

Besonders mit dem Layout von Qt habe ich noch meine Probleme, da ich vorher auch nie mit Qt gearbeitet habe.

Skills zum Semesterstart:

Python: 3 %

Qt: 2%

Skills zur Abgabe:

Python: 65 %

Qt: 15 % 

Das Projekt wird in den kommenden Wochen spaßeshalber vervollständigt.
