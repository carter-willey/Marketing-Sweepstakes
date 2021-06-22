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
        user_input = int(input(prompt))
        return user_input

    @staticmethod
    def display_contestant_info(contestant):
        print(f"#{contestant.registration_number} {contestant.first_name} {contestant.last_name} and their email is {contestant.email}")

    @staticmethod
    def display_sweepstakes_info(sweepstakes):
        pass

    @staticmethod
    def display_sweepstakes_selection_menu(all_sweepstakes):
        pass

    @staticmethod
    def display_marketing_firm_menu_options(marketing_firm_name):
        pass

    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes):
        pass