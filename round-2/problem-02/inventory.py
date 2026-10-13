class Inventory:
    def __init__(self, quantities=None):
        self.quantities = dict(quantities or {})
        self.reservations = {}

    def reserve(self, order_id, item, quantity):
        available = self.quantities.get(item, 0)
        if quantity <= 0 or available < quantity:
            return False
        self.quantities[item] = available - quantity
        self.reservations[order_id] = (item, quantity)
        return True

    def release(self, order_id):
        reservation = self.reservations.pop(order_id, None)
        if reservation:
            item, quantity = reservation
            self.quantities[item] = self.quantities.get(item, 0) + quantity
            return True
        return False
