class UserInterface:
    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def get_user_input_string(prompt):
        user_input = input(prompt)
        return user_input

    @staticmethod
    def get_user_input_int(prompt):
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("please enter a number!")
            return UserInterface.get_user_input_int(prompt)

    @staticmethod
    def display_contestant_info(contestant):
        print(f"Contestant #{contestant.registration_number} is {contestant.first_name} {contestant.last_name} and their email is {contestant.email}")

    @staticmethod
    def display_sweepstakes_info(sweepstakes):
        pass

    @staticmethod
    def display_sweepstakes_selection_menu(all_sweepstakes):
        # LIST OUT ALL SWEEPSTAKES
        i = 1   #for displaying in terminal
        print("Which sweepstake would you like to interact with?:")
        for sweepstake in all_sweepstakes:
            print(f"{i}: {sweepstake.name}")

    @staticmethod
    def display_marketing_firm_menu_options(marketing_firm_name):
        print(f"\t\t-Hello, {marketing_firm_name}.-")
        print("\tPress -1- to create a sweepstakes")
        print("\tPress -2- to select a sweepstakes")
        print("\tPress -3- to change your marketing firm's name")
        print("\tPress -4- to terminate the program")

    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes):
        print(f"\t\t-{sweepstakes.name} menu-")
        print("\tPress -1- to register a contestant")
        print("\tPress -2- to view contestants")
        print("\tPress -3- to pick a winner")
        print("\tPress -4- to go back to all sweepstakes")
