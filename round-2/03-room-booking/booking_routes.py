OPENS_AT = 8 * 60
CLOSES_AT = 22 * 60
MAX_MINUTES = 120


def parse_time(text):
    hours, minutes = text.split(":")
    return int(hours) * 60 + int(minutes)


class BookingRoutes:
    def __init__(self, bookings):
        self.bookings = bookings

    def create(self, payload):
        required = ("booking_id", "room", "student_id", "start", "end")
        if any(key not in payload for key in required):
            return {"status": 400}
        try:
            start = parse_time(payload["start"])
            end = parse_time(payload["end"])
        except (ValueError, AttributeError):
            return {"status": 400}
        if start >= end or start < OPENS_AT or end > CLOSES_AT or end - start > MAX_MINUTES:
            return {"status": 400}
        booking, reason = self.bookings.book(payload["booking_id"], payload["room"], payload["student_id"], start, end)
        if booking:
            return {"status": 201, "booking_id": booking.booking_id}
        return {"status": 404 if reason == "unknown room" else 409}

    def cancel(self, payload):
        if self.bookings.cancel(payload.get("booking_id"), payload.get("student_id")):
            return {"status": 200}
        return {"status": 404}
