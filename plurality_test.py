from voting_data import VotingData
from plurality import Plurality

# Create VotingData object and read data
voting_data = VotingData()


# Create Plurality object and determine winner
plurality = Plurality()
plurality.determine_winner(voting_data)

# Print Plurality winner
print(f'Plurality Winner: {plurality.plurality_winner}')