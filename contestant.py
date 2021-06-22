from userinterface import UserInterface
class Contestant:
    def __init__(self):
        self.first_name = UserInterface.get_user_input_string("Please enter your first name: ")
        self.last_name = UserInterface.get_user_input_string("Please enter your last name: ")
        self.email = UserInterface.get_user_input_string("Please enter your email address: ")
        self.registration_number = 0
    def notify(self, is_winner):
        pass