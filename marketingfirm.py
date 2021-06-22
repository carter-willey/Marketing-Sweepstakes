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
        #display sweepstakes and promt which one they would like, then open the menu for that sweepstake
        pass
    def menu(self):

        pass