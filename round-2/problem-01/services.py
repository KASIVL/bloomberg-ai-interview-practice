from models import Registration


class RegistrationService:
    def __init__(self, repository):
        self.repository = repository

    def register(self, event_id, student_id, registration_id):
        event = self.repository.get_event(event_id)
        if event is None:
            return False
        registrations = self.repository.for_event(event_id)
        if len(registrations) >= event.capacity:
            return False
        if self.repository.active_for_student(event_id, student_id):
            return False
        self.repository.save_registration(Registration(registration_id, event_id, student_id))
        return True

    def cancel(self, registration_id):
        registration = self.repository.get_registration(registration_id)
        if registration is None or registration.status != "active":
            return False
        registration.status = "cancelled"
        return True
