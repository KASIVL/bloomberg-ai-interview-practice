import unittest
from scheduler import is_available


class SchedulerTests(unittest.TestCase):
    def test_conflicting_event_is_rejected(self):
        self.assertFalse(is_available([(10, 12)], 11, 13))

    def test_adjacent_events_conflict(self):
        self.assertFalse(is_available([(10, 12)], 12, 14))

    def test_invalid_interval_is_rejected(self):
        self.assertFalse(is_available([], 5, 5))

    def test_available_check_does_not_change_existing_events(self):
        events = [(1, 2)]
        is_available(events, 3, 4)
        self.assertEqual(events, [(1, 2)])

    def test_conflict_does_not_add_event(self):
        events = [(10, 12)]
        is_available(events, 11, 13)
        self.assertEqual(events, [(10, 12)])


if __name__ == "__main__":
    unittest.main()
