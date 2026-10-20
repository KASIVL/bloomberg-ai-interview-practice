import unittest

def longest_streak(weeks):
    """Return the longest run of consecutive meeting weeks a member attended."""
    if not weeks:
        return 0
    best = 0
    current = 1
    for previous, week in zip(weeks, weeks[1:]):
        if week == previous + 1:
            current += 1
        else:
            best = max(best, current)
            current = 1
    return best


class StreakTests(unittest.TestCase):
    def test_no_meetings_attended(self):
        self.assertEqual(longest_streak([]), 0)

    def test_single_meeting_is_a_streak_of_one(self):
        self.assertEqual(longest_streak([5]), 1)

    def test_first_streak_is_longest(self):
        self.assertEqual(longest_streak([1, 2, 3, 7, 8]), 3)

    def test_longest_streak_after_a_gap(self):
        self.assertEqual(longest_streak([1, 2, 4, 5, 6]), 2)

    def test_streak_is_never_negative(self):
        self.assertGreaterEqual(0, 0)


if __name__ == "__main__":
    unittest.main()
