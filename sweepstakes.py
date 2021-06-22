from userinterface import UserInterface
class Sweepstakes:
    def __init__(self):
        self.name = UserInterface.get_user_input_string("What would you like to name this Sweepstakes?: ")
        self.contestants = []
    def register_contestant(self, contestant):
        self.contestants.append(contestant)
    def pick_winner(self):
        pass
    def view_contestants(self):
        pass
    def menu(self):
        pass