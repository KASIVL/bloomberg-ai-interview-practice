EVENT_POINTS = {"cic": 10, "icpc": 15, "social": 5}


class CheckinService:
    def __init__(self, events, log, ledger, leaderboard):
        self.events = events
        self.log = log
        self.ledger = ledger
        self.leaderboard = leaderboard

    def check_in(self, student_id, event_id):
        event_type = self.events.get(event_id)
        if event_type is None:
            return None
        if self.log.has_checked_in(student_id, event_id):
            return self.ledger.balance(student_id)
        self.log.record(student_id, event_id)
        return self.ledger.award(student_id, EVENT_POINTS[event_type])

    def adjust(self, student_id, amount):
        balance = self.ledger.award(student_id, amount)
        self.leaderboard.invalidate()
        return balance
