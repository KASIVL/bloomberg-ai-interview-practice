class CheckinRoutes:
    def __init__(self, checkins, leaderboard):
        self.checkins = checkins
        self.leaderboard = leaderboard

    def check_in(self, payload):
        if "student_id" not in payload or "event_id" not in payload:
            return {"status": 400}
        balance = self.checkins.check_in(payload["student_id"], payload["event_id"])
        if balance is None:
            return {"status": 404}
        return {"status": 200, "points": balance}

    def top(self, n=3):
        ranked = self.leaderboard.top(n)
        return {"status": 200, "leaders": [{"student_id": student_id, "points": points} for student_id, points in ranked]}
