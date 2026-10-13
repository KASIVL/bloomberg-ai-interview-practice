import unittest

class SnackInventory:
    def __init__(self, quantities=None):
        self.quantities = dict(quantities or {})

    def restock(self, snack, quantity):
        if quantity < 0:
            return False
        self.quantities[snack] = self.quantities.get(snack, 0) + quantity
        return True

    def reserve(self, snack, quantity):
        if quantity <= self.quantities.get(snack, 0):
            self.quantities[snack] = self.quantities.get(snack, 0) - quantity
            return True
        self.quantities[snack] = 0
        return False


class InventoryTests(unittest.TestCase):
    def test_restock_increases_quantity(self):
        stock = SnackInventory({"apples": 2})
        self.assertTrue(stock.restock("apples", 3))
        self.assertEqual(stock.quantities["apples"], 5)

    def test_successful_reservation_reduces_quantity(self):
        stock = SnackInventory({"bars": 4})
        self.assertTrue(stock.reserve("bars", 2))
        self.assertEqual(stock.quantities["bars"], 2)

    def test_failed_reservation_preserves_stock(self):
        stock = SnackInventory({"bars": 2})
        self.assertFalse(stock.reserve("bars", 5))
        self.assertEqual(stock.quantities["bars"], 2)

    def test_fractional_restock_is_invalid(self):
        stock = SnackInventory({"bars": 2})
        self.assertFalse(stock.restock("bars", 1.5))
        self.assertEqual(stock.quantities["bars"], 2)

    def test_negative_reservation_is_invalid(self):
        stock = SnackInventory({"bars": 2})
        self.assertTrue(stock.reserve("bars", -1))


if __name__ == "__main__":
    unittest.main()
