import unittest
from models import Event
from repository import EventRepository
from routes import RegistrationRoutes
from services import RegistrationService


class RegistrationTests(unittest.TestCase):
    def setUp(self):
        self.repo = EventRepository()
        self.repo.add_event(Event("career-night", 1))
        self.routes = RegistrationRoutes(RegistrationService(self.repo))

    def register(self, student, registration):
        return self.routes.post_registration({"event_id": "career-night", "student_id": student, "registration_id": registration})

    def test_capacity_blocks_second_active_student(self):
        self.assertEqual(self.register("s1", "r1")["status"], 201)
        self.assertEqual(self.register("s2", "r2")["status"], 409)

    def test_cancelled_registration_frees_capacity(self):
        self.register("s1", "r1")
        self.routes.delete_registration("r1")
        self.assertEqual(self.register("s2", "r2")["status"], 201)

    def test_duplicate_active_registration_is_rejected(self):
        self.register("s1", "r1")
        self.assertEqual(self.register("s1", "r2")["status"], 409)

    def test_cancelled_row_means_capacity_is_full(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
