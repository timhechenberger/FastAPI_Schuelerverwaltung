# FastAPI_Schuelerverwaltung

School project (NSCS)

## Beschreibung
Einfache **Schülerverwaltungs-API** mit **FastAPI** (REST) und einem **gRPC Service** für Datumsberechnungen.  
Daten werden dauerhaft in einer JSON-Datei gespeichert.

## Update
- Erweiterung um **Docker Compose**
- **FastAPI** und **gRPC Service** laufen jeweils in einem eigenen Container
- gRPC-Port ist nur intern zwischen den Containern erreichbar (kein Port-Mapping nach außen)

## Funktionen
- Schüler erstellen, anzeigen, ändern, löschen
- Beispieldaten über Initialisierungs-Endpunkt erzeugen
- gRPC `CalcDateDelta`: berechnet Alter, Schuldauer und Tage bis zur Matura (Datumsformat: `YYYY-MM-DD`)

## Technologien
- Python, FastAPI, Uvicorn, gRPC / Protocol Buffers, venv, JSON-Dateispeicherung, Docker Compose

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

## Docker Compose (Start/Stop)
```bash
docker compose up --build -d   # startet beide Container
docker compose down            # stoppt beide Container
```

Logs anzeigen:
```bash
docker compose logs -f
```

## Swagger
http://localhost:8000/docs
