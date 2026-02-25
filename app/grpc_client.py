import grpc
import sys, os

# Pfad zu den generierten Proto-Dateien
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'grpc_service')))

import date_service_pb2
import date_service_pb2_grpc

def calc_date_delta(birth_date: str, entry_date: str, current_date: str, matura_date: str):
    channel = grpc.insecure_channel("localhost:50051")
    stub = date_service_pb2_grpc.DateServiceStub(channel)
    response = stub.CalcDateDelta(date_service_pb2.DateDeltaRequest(
        birth_date=birth_date,
        entry_date=entry_date,
        current_date=current_date,
        matura_date=matura_date
    ))
    return {
        "age_in_days": response.age_in_days,
        "days_in_school": response.days_in_school,
        "days_until_matura": response.days_until_matura
    }