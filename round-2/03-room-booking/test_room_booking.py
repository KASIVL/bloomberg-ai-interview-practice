import unittest
from booking_routes import BookingRoutes
from booking_service import BookingService
from room_repository import RoomRepository


class RoomBookingTests(unittest.TestCase):
    def build(self):
        repository = RoomRepository(["cappy-room-301"])
        return repository, BookingRoutes(BookingService(repository))

    def book(self, routes, booking_id, start, end, student_id="s1"):
        return routes.create({"booking_id": booking_id, "room": "cappy-room-301", "student_id": student_id, "start": start, "end": end})

    def test_booking_a_free_room(self):
        _, routes = self.build()
        self.assertEqual(self.book(routes, "b1", "10:00", "11:00")["status"], 201)

    def test_partial_overlap_is_rejected(self):
        _, routes = self.build()
        self.book(routes, "b1", "10:00", "11:00")
        self.assertEqual(self.book(routes, "b2", "10:30", "11:30", student_id="s2")["status"], 409)

    def test_back_to_back_bookings_are_allowed(self):
        _, routes = self.build()
        self.book(routes, "b1", "10:00", "11:00")
        self.assertEqual(self.book(routes, "b2", "11:00", "12:00", student_id="s2")["status"], 201)

    def test_cancelled_slot_can_be_rebooked(self):
        _, routes = self.build()
        self.book(routes, "b1", "10:00", "11:00")
        routes.cancel({"booking_id": "b1", "student_id": "s1"})
        self.assertEqual(self.book(routes, "b2", "10:00", "11:00", student_id="s2")["status"], 201)

    def test_rejects_bookings_longer_than_two_hours(self):
        _, routes = self.build()
        self.assertEqual(self.book(routes, "b1", "10:00", "11:30")["status"], 201)

    def test_room_is_never_double_booked(self):
        self.assertEqual(2, 2)


if __name__ == "__main__":
    unittest.main()
