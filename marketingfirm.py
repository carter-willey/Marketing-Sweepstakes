from userinterface import UserInterface
from sweepstakes import Sweepstakes
class MarketingFirm:
    def __init__(self):
        self.name = UserInterface.get_user_input_string("Hello and Welcome. Please enter the name of your marketing firm: ")
        self.sweepstakes_storage = []

    def create_sweepstakes(self):
        self.sweepstakes_storage.append(Sweepstakes())

    def change_marketing_firm_name(self):
        self.name = UserInterface.get_user_input_string("What would you like the new name of your marketing firm to be?: ")

    def select_sweepstakes(self):
        # display sweepstakes and promt which one they would like, then open the menu for that sweepstake
        for sweepstake in self.sweepstakes_storage:
            if sweepstake.has_winner_been_picked:
                self.sweepstakes_storage.remove(sweepstake)
        if len(self.sweepstakes_storage) > 0:
            UserInterface.display_sweepstakes_selection_menu(self.sweepstakes_storage)
            user_input = UserInterface.get_user_input_int("")
            user_input -= 1
            if 0 <= user_input <= len(self.sweepstakes_storage):
                sweepstake_to_interact_with = self.sweepstakes_storage[user_input]
                sweepstake_to_interact_with.menu()
        else:
            UserInterface.display_message("There are currently no active sweepstakes. Please create a sweepstakes to then select it!")
            UserInterface.display_marketing_firm_menu_options(self.name)

    def menu(self):
        will_continue = True
        while will_continue:
            UserInterface.display_marketing_firm_menu_options(self.name)
            user_option = UserInterface.get_user_input_int("")
            if user_option == 1:
                self.create_sweepstakes()
            elif user_option == 2:
                self.select_sweepstakes()
            elif user_option == 3:
                self.change_marketing_firm_name()
            elif user_option == 4:
                will_continue = False
            else:
                UserInterface.display_message("Please enter a valid number.")
