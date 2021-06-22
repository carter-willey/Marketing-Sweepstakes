from userinterface import UserInterface
from contestant import Contestant
from sweepstakes import Sweepstakes
sweepstake = Sweepstakes()


contestant1 = Contestant("carter", "willey", "cjwilley23")
contestant2 = Contestant("john", "doe", "jd23")
contestant3 = Contestant("jane", "doe", "janedoe23")
sweepstake.register_contestant(contestant1)
sweepstake.register_contestant(contestant2)
sweepstake.register_contestant(contestant3)
sweepstake.view_contestants()
sweepstake.pick_winner()