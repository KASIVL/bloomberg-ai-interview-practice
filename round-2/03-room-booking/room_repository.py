class RoomRepository:
    def __init__(self, rooms):
        self.rooms = set(rooms)
        self.bookings = {}

    def has_room(self, room):
        return room in self.rooms

    def get(self, booking_id):
        return self.bookings.get(booking_id)

    def save(self, booking):
        self.bookings[booking.booking_id] = booking
        return booking

    def bookings_for_room(self, room):
        return [booking for booking in self.bookings.values() if booking.room == room]
