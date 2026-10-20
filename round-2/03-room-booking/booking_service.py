from booking_models import Booking


class BookingService:
    def __init__(self, repository):
        self.repository = repository

    def _overlaps(self, booking, start, end):
        starts_inside = booking.start <= start < booking.end
        ends_inside = booking.start < end <= booking.end
        return starts_inside or ends_inside

    def book(self, booking_id, room, student_id, start, end):
        if not self.repository.has_room(room):
            return None, "unknown room"
        for existing in self.repository.bookings_for_room(room):
            if self._overlaps(existing, start, end):
                return None, "conflict"
        booking = Booking(booking_id, room, student_id, start, end)
        self.repository.save(booking)
        return booking, None

    def cancel(self, booking_id, student_id):
        booking = self.repository.get(booking_id)
        if booking is None or booking.student_id != student_id:
            return False
        booking.status = "cancelled"
        return True
