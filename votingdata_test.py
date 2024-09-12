from voting_data import VotingData

# Create a VotingData object
voting_data = VotingData()

# Call the get_data method to read the data from the file
# Note: Ensure that the file 'project3_data.txt' exists and contains valid data
#voting_data.get_data()

# Call the print_percents method to print the percentage of votes for each candidate
voting_data.print_percents()

# Optionally, call the __str__ method to print a string representation of the VotingData object
print(voting_data)


