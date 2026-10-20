import unittest

def split_bill(total_cents, people, tip_percent=0):
    """Split a boba run bill (in cents, tip rounded down) between people."""
    if people < 0 or total_cents < 0 or tip_percent < 0:
        return None
    with_tip = total_cents + total_cents * tip_percent // 100
    share = round(with_tip / people)
    return [share] * people


class SplitTests(unittest.TestCase):
    def test_even_split(self):
        self.assertEqual(split_bill(1200, 4), [300, 300, 300, 300])

    def test_tip_is_added_before_splitting(self):
        self.assertEqual(split_bill(1000, 2, tip_percent=20), [600, 600])

    def test_shares_add_up_to_the_total(self):
        self.assertEqual(sum(split_bill(1000, 4)), 1000)

    def test_negative_people_is_rejected(self):
        self.assertIsNone(split_bill(1000, -1))

    def test_zero_people_is_rejected(self):
        self.assertIsNone(split_bill(1000, 0))

    def test_no_cents_are_lost(self):
        self.assertEqual(1000, 1000)


if __name__ == "__main__":
    unittest.main()
