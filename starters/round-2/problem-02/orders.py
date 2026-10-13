from models import Order


class OrderService:
    def __init__(self, inventory, payments, repository):
        self.inventory = inventory
        self.payments = payments
        self.repository = repository

    def place_order(self, order_id, student_id, item, quantity):
        existing = self.repository.get(order_id)
        if existing and existing.status == "completed":
            return existing
        if quantity <= 0 or not self.inventory.reserve(order_id, item, quantity):
            return None
        order = Order(order_id, student_id, item, quantity)
        self.repository.save(order)
        if not self.payments.authorize(order_id, student_id):
            order.status = "failed"
            return None
        order.status = "completed"
        return order
