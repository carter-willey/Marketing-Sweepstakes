from contestant import Contestant
from userinterface import UserInterface
import random

class Sweepstakes:
    def __init__(self):
        self.name = UserInterface.get_user_input_string("What would you like to name this Sweepstakes?: ")
        self.contestants = {}
        self.has_winner_been_picked = False

    def register_contestant(self, contestant):
        contestant.registration_number = len(self.contestants)
        self.contestants.update({len(self.contestants): contestant})

    def pick_winner(self):
        random_winner = self.contestants[random.randint(0, len(self.contestants)-1)]
        random_winner.is_winner = True
        self.has_winner_been_picked = True
        for contestant in self.contestants.values():
            contestant.notify()
        UserInterface.display_message("Since a winner has been selected, this sweepstake will no longer be active!")

    def view_contestants(self):
        for contestant in self.contestants.values():
            UserInterface.display_contestant_info(contestant)

    def menu(self):
        will_continue = True
        while will_continue:
            UserInterface.display_sweepstakes_menu_options(self)
            user_option = UserInterface.get_user_input_int("")
            if user_option == 1:
                self.register_contestant(Contestant())
            elif user_option == 2:
                self.view_contestants()
            elif user_option == 3:
                self.pick_winner()
            elif user_option == 4:
                will_continue = False
            else:
                UserInterface.display_message("Please enter a valid number.")

