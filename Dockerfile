FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY grpc_service ./grpc_service

# Proto-Dateien neu generieren (überschreibt die vorgenerierte Version)
RUN python -m grpc_tools.protoc \
    -I./grpc_service \
    --python_out=./grpc_service \
    --grpc_python_out=./grpc_service \
    ./grpc_service/date_service.proto

RUN mkdir /data

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
