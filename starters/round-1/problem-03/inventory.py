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
