from voting_data import VotingData
from instant_run_off import InstantRunOff
from majority import Majority


voting_data = VotingData()

instant_run_off = InstantRunOff()

instant_run_off.determine_winner(voting_data)



