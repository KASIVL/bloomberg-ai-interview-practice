from dataclasses import dataclass


@dataclass
class Booking:
    booking_id: str
    room: str
    student_id: str
    start: int  # minutes after midnight
    end: int  # minutes after midnight
    status: str = "active"
