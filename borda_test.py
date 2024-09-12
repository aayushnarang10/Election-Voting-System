from voting_data import VotingData
from borda import Borda

voting_data = VotingData()




borda = Borda()

borda.print_points()

borda.determine_winner(voting_data.votes)








