from userinterface import UserInterface
class Contestant:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.registration_number = 0
    def notify(self, is_winner):
        pass