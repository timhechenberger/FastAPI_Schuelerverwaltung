# FastAPI_Schuelerverwaltung

School project (NSCS)

## Beschreibung
Dieses Projekt ist eine einfache **Schülerverwaltungs-API**, die mit **FastAPI** in Python umgesetzt wurde.  
Über eine REST-Schnittstelle können Schüler angelegt, abgefragt, geändert und gelöscht werden.

Die Anwendung speichert die Daten dauerhaft in einer **JSON-Datei** und lädt diese beim Start automatisch wieder ein.

## Funktionen
- Schüler erstellen
- Alle Schüler anzeigen
- Einzelnen Schüler per ID abrufen
- Schülerdaten ändern
- Schüler löschen
- Beispieldaten über einen Initialisierungs-Endpunkt erzeugen

## Technologien
- Python
- FastAPI
- Uvicorn
- Virtual Environment (venv)
- JSON-Dateispeicherung

## Installation
pip install fastapi uvicorn