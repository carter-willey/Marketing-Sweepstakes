from userinterface import UserInterface
class Contestant:
    def __init__(self):
        self.first_name = UserInterface.get_user_input_string("What is your first name?: ")
        self.last_name = UserInterface.get_user_input_string("What is your last name?: ")
        self.email = UserInterface.get_user_input_string("What is your first email address?: ")
        self.registration_number = 0
        self.is_winner = False

    def notify(self):
        if self.is_winner:
            UserInterface.display_message(f"{self.first_name} {self.last_name} is a Winner! Congratulations")
        else:
            UserInterface.display_message(f"{self.first_name} {self.last_name}, better luck next time!")