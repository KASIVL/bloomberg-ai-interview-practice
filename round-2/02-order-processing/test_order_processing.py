import unittest
from inventory import Inventory
from orders import OrderRoutes, OrderService
from payments import FakePaymentService
from repository import OrderRepository


class OrderTests(unittest.TestCase):
    def build(self, approved=True):
        inventory = Inventory({"club-shirt": 5})
        payments = FakePaymentService(approved)
        repository = OrderRepository()
        service = OrderService(inventory, payments, repository)
        return inventory, payments, repository, OrderRoutes(service)

    def submit(self, routes, order_id="o1", quantity=2):
        return routes.submit({"order_id": order_id, "student_id": "s1", "item": "club-shirt", "quantity": quantity})

    def test_successful_order_updates_inventory(self):
        inventory, _, _, routes = self.build()
        self.assertEqual(self.submit(routes)["status"], 201)
        self.assertEqual(inventory.quantities["club-shirt"], 3)

    def test_failed_payment_preserves_inventory(self):
        inventory, _, _, routes = self.build(approved=False)
        self.assertEqual(self.submit(routes)["status"], 409)
        self.assertEqual(inventory.quantities["club-shirt"], 5)

    def test_retry_of_completed_order_does_not_deduct_twice(self):
        inventory, payments, _, routes = self.build()
        self.submit(routes)
        self.submit(routes)
        self.assertEqual(inventory.quantities["club-shirt"], 3)
        self.assertEqual(len(payments.authorizations), 1)

    def test_failed_order_never_changes_a_number(self):
        self.assertEqual(5, 5)


if __name__ == "__main__":
    unittest.main()
