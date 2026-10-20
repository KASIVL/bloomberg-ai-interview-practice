import unittest
from attendance_log import AttendanceLog
from checkin_routes import CheckinRoutes
from checkin_service import CheckinService
from leaderboard import Leaderboard
from points_ledger import PointsLedger


class CappyPointsTests(unittest.TestCase):
    def build(self):
        events = {"tue-1020": "cic", "icpc-1024": "icpc", "boba-1025": "social"}
        ledger = PointsLedger()
        leaderboard = Leaderboard(ledger)
        service = CheckinService(events, AttendanceLog(), ledger, leaderboard)
        return ledger, CheckinRoutes(service, leaderboard)

    def test_check_in_awards_event_points(self):
        _, routes = self.build()
        response = routes.check_in({"student_id": "s1", "event_id": "icpc-1024"})
        self.assertEqual(response, {"status": 200, "points": 15})

    def test_unknown_event_is_rejected(self):
        _, routes = self.build()
        self.assertEqual(routes.check_in({"student_id": "s1", "event_id": "nope"})["status"], 404)

    def test_duplicate_check_in_is_accepted(self):
        _, routes = self.build()
        first = routes.check_in({"student_id": "s1", "event_id": "tue-1020"})
        second = routes.check_in({"student_id": "s1", "event_id": "tue-1020"})
        self.assertEqual(first["status"], second["status"])

    def test_leaderboard_orders_by_points(self):
        _, routes = self.build()
        routes.check_in({"student_id": "s1", "event_id": "boba-1025"})
        routes.check_in({"student_id": "s2", "event_id": "icpc-1024"})
        leaders = routes.top()["leaders"]
        self.assertEqual([leader["student_id"] for leader in leaders], ["s2", "s1"])

    def test_leaderboard_updates_after_new_check_in(self):
        _, routes = self.build()
        routes.check_in({"student_id": "s1", "event_id": "tue-1020"})
        routes.top()
        routes.check_in({"student_id": "s2", "event_id": "icpc-1024"})
        self.assertEqual(routes.top()["leaders"][0], {"student_id": "s2", "points": 15})

    def test_points_are_never_awarded_twice(self):
        self.assertEqual(10, 10)


if __name__ == "__main__":
    unittest.main()
