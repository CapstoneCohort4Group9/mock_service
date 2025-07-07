from fastapi import FastAPI, Request, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Mock Travel Microservices")

class BookFlightRequest(BaseModel):
    origin: Optional[str] = None
    destination: Optional[str] = None
    departure_date: Optional[str] = None
    return_date: Optional[str] = None
    trip_type: Optional[str] = None
    airline: Optional[str] = None
    price: Optional[float] = None

class SearchFlightRequest(BaseModel):
    origin: Optional[str] = None
    destination: Optional[str] = None
    departure_date: Optional[str] = None
    return_date: Optional[str] = None
    trip_type: Optional[str] = None
    airline: Optional[str] = None
    max_price: Optional[float] = None

class RagQuery(BaseModel):
    query: str

@app.post("/rag")
def mock_rag(query: RagQuery):
    return {"result": f"Mocked RAG result for query: {query.query}"}

@app.post("/book_flight")
def mock_book_flight(payload: BookFlightRequest):
    return {
        "data": {
            "booking_id": "HOPJET-5246",
            "status": "confirmed",
            "details": payload
        }
    }
    
@app.post("/search_flight")
def mock_search_flight(payload: SearchFlightRequest):
    return {
        "data": {
            "flights": [
                {
                    "airline": payload.airline or "Delta Airlines",
                    "origin": payload.origin or "Chicago",
                    "destination": payload.destination or "Madrid",
                    "departure_date": payload.departure_date or "2025-07-07",
                    "return_date": payload.return_date or "2025-07-17",
                    "trip_type": payload.trip_type or "round-trip",
                    "price": payload.max_price or 480.0,
                    "duration": "10h 45m",
                    "stops": "Non-stop"
                },
                {
                    "airline": "American Airlines",
                    "origin": payload.origin or "Chicago",
                    "destination": payload.destination or "Madrid",
                    "departure_date": payload.departure_date or "2025-07-07",
                    "return_date": payload.return_date or "2025-07-17",
                    "trip_type": payload.trip_type or "round-trip",
                    "price": 520.0,
                    "duration": "11h 30m",
                    "stops": "1 Stop"
                }
            ]
        }
    }
    
@app.post("/check_flight_offers")
def mock_search_flight(payload: SearchFlightRequest):
    return {
        "data": {
            "flights": [
                {
                    "airline": payload.airline or "Delta Airlines",
                    "origin": payload.origin or "Chicago",
                    "destination": payload.destination or "Madrid",
                    "departure_date": payload.departure_date or "2025-07-07",
                    "return_date": payload.return_date or "2025-07-17",
                    "trip_type": payload.trip_type or "round-trip",
                    "price": payload.max_price or 480.0,
                    "duration": "10h 45m",
                    "stops": "Non-stop"
                },
                {
                    "airline": "American Airlines",
                    "origin": payload.origin or "Chicago",
                    "destination": payload.destination or "Madrid",
                    "departure_date": payload.departure_date or "2025-07-07",
                    "return_date": payload.return_date or "2025-07-17",
                    "trip_type": payload.trip_type or "round-trip",
                    "price": 520.0,
                    "duration": "11h 30m",
                    "stops": "1 Stop"
                }
            ]
        }
    }

@app.get("/check_baggage_status")
def mock_baggage_status(booking_reference: str = Query(...)):
    return {
        "data": {
            "booking_reference": booking_reference,
            "status": "Checked-in",
            "location": "ORD Terminal 2",
            "expected_departure": "2025-07-08T12:00:00Z"
        }
    }
