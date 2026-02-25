# FastAPI_Schuelerverwaltung

School project (NSCS)

## Beschreibung
Einfache **Schülerverwaltungs-API** mit **FastAPI** (REST) und einem **gRPC Service** für Datumsberechnungen.  
Daten werden dauerhaft in einer JSON-Datei gespeichert.

## Funktionen
- Schüler erstellen, anzeigen, ändern, löschen
- Beispieldaten über Initialisierungs-Endpunkt erzeugen
- gRPC `CalcDateDelta`: berechnet Alter, Schuldauer und Tage bis zur Matura (Datumsformat: `YYYY-MM-DD`)

## Technologien
- Python, FastAPI, Uvicorn, gRPC / Protocol Buffers, venv, JSON-Dateispeicherung

## Installation
```bash
pip install fastapi uvicorn grpcio grpcio-tools
```

Proto-Dateien generieren (im `grpc_service` Ordner):
```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. date_service.proto
```

## How to run
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000     # FastAPI  (Port 8000)
python grpc_service/server.py                       # gRPC     (Port 50051)
python grpc_service/client_test.py                  # gRPC testen
```

## How to run Docker
```bash
docker run -p 8000:8000 -v ${PWD}/data:/data schueler-api
docker build -f Dockerfile.grpc -t schueler-grpc . && docker run -p 50051:50051 schueler-grpc
```

## Swagger
http://localhost:8000/docs
