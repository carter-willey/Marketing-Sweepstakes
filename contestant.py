import smtplib

from userinterface import UserInterface
import smtpd
sender_email = "pythontestbotlol@gmail.com"
sender_password = "reallycleverpassword1"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, sender_password)

class Contestant:
    def __init__(self):
        self.first_name = UserInterface.get_user_input_string("What is your first name?: ")
        self.last_name = UserInterface.get_user_input_string("What is your last name?: ")
        self.email = UserInterface.get_user_input_string("What is your first email address?: ")
        self.registration_number = 0
        self.is_winner = False

    def notify(self):

        if self.is_winner:
            server.sendmail(sender_email, self.email, f"{self.first_name} {self.last_name} is a Winner! Congratulations")
            UserInterface.display_message(f"{self.first_name} {self.last_name} is a Winner! Congratulations")
        else:
            server.sendmail(sender_email, self.email, f"{self.first_name} {self.last_name}, better luck next time!")
            UserInterface.display_message(f"{self.first_name} {self.last_name}, better luck next time!")