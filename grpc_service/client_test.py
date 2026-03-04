import grpc
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'grpc_service')))

import date_service_pb2
import date_service_pb2_grpc

def test_calc():
    # Verbindung zum gRPC Server
    channel = grpc.insecure_channel("localhost:50051")
    stub = date_service_pb2_grpc.DateServiceStub(channel)

    # Anfrage senden
    response = stub.CalcDateDelta(date_service_pb2.DateDeltaRequest(
        birth_date="2006-05-01",
        entry_date="2021-09-01",
        current_date="2025-02-25",
        matura_date="2026-06-15"
    ))

    print(f"Alter in Tagen:          {response.age_in_days}")
    print(f"Tage in der Schule:      {response.days_in_school}")
    print(f"Tage bis zur Matura:     {response.days_until_matura}")

if __name__ == "__main__":
    test_calc()