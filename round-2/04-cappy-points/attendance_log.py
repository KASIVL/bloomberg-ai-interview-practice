class AttendanceLog:
    def __init__(self):
        self.seen = set()
        self.entries = []

    def has_checked_in(self, student_id, event_id):
        return (student_id, event_id) in self.seen

    def record(self, student_id, event_id):
        self.seen.add((event_id, student_id))
        self.entries.append((student_id, event_id))
