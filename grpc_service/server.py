import grpc
from concurrent import futures
from datetime import datetime, date
import sys
import os

# Damit Python die generierten Dateien findet
sys.path.insert(0, os.path.dirname(__file__))

import date_service_pb2
import date_service_pb2_grpc

# Implementierung des gRPC DateService
class DateServiceServicer(date_service_pb2_grpc.DateServiceServicer):
    

    def CalcDateDelta(self, request, context):
        try:
            # Datumstrings parsen (Format: YYYY-MM-DD)
            birth_date  = datetime.strptime(request.birth_date,  "%Y-%m-%d").date()
            entry_date  = datetime.strptime(request.entry_date,  "%Y-%m-%d").date()
            current_date = datetime.strptime(request.current_date, "%Y-%m-%d").date()
            matura_date = datetime.strptime(request.matura_date, "%Y-%m-%d").date()

            # Berechnungen
            age_in_days        = (current_date - birth_date).days
            days_in_school     = (current_date - entry_date).days
            days_until_matura  = (matura_date - current_date).days

            return date_service_pb2.DateDeltaResponse(
                age_in_days=age_in_days,
                days_in_school=days_in_school,
                days_until_matura=days_until_matura
            )

        except ValueError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(f"Ungültiges Datumsformat: {e}")
            return date_service_pb2.DateDeltaResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    date_service_pb2_grpc.add_DateServiceServicer_to_server(
        DateServiceServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    print("gRPC Server läuft auf Port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
