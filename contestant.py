from userinterface import UserInterface
class Contestant:
    def __init__(self):
        self.first_name = UserInterface.get_user_input_string("What is your first name?: ")
        self.last_name = UserInterface.get_user_input_string("What is your last name?: ")
        self.email = UserInterface.get_user_input_string("What is your first email address?: ")
        self.registration_number = 0
    def notify(self, is_winner):
        pass