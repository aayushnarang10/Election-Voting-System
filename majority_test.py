from voting_data import VotingData
from majority import Majority

# Create a VotingData object and populate it with sample data
voting_data = VotingData()



# Create a Majority object
majority = Majority()

# Determine the winner using the voting data
majority.determine_winner(voting_data)

# Print the result
print(majority)