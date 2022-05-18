from datetime import date


class Person:
    def __init__(self, first_name: str, last_name: str, date_birth: date):
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth = date_birth
