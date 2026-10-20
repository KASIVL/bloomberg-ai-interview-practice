class Leaderboard:
    def __init__(self, ledger):
        self.ledger = ledger
        self._ranked = None

    def top(self, n=3):
        if self._ranked is None:
            self._ranked = sorted(self.ledger.balances.items(), key=lambda item: (-item[1], item[0]))
        return self._ranked[:n]

    def invalidate(self):
        self._ranked = None
