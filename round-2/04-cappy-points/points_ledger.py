class PointsLedger:
    def __init__(self):
        self.balances = {}

    def award(self, student_id, amount):
        self.balances[student_id] = self.balances.get(student_id, 0) + amount
        return self.balances[student_id]

    def balance(self, student_id):
        return self.balances.get(student_id, 0)
