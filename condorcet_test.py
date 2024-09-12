from voting_data import VotingData
from condorcet import Condorcet

# Step 1: Create a VotingData object
voting_data = VotingData()

# Step 2: Instantiate a Condorcet object
condorcet = Condorcet()

# Step 3: Determine the Condorcet winner
condorcet.determine_winner(voting_data)


condorcet.print_wins()

