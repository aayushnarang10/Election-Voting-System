'''
The Plurality Voting Method is a voting method that selects the 
candidate with the most #1 choice votes.
If there is a tie, there is no Plurality winner.

The Plurality class inherits from the Majority class.
The Plurality class has the following attributes:
    plurality_winner: a string representing the Plurality winner
The Plurality class has the following methods:
    __init__: initializes the Plurality object
    __str__: returns a string representation of the Plurality object
    determine_winner: determines the winner of the election using the 
    Plurality voting method
'''

from voting_data import VotingData
from majority import Majority

class Plurality(Majority):
    def __init__(self):
        '''
        The __init__ method initializes the Plurality object.
        The Plurality object inherits from the Majority object.
        The Plurality object has the following attributes:
            plurality_winner: a string representing the Plurality winner
                              set the attribute to an empty string
        Parameters:
            self: a Plurality object
        Returns:
            None
        '''
        
        super().__init__()
        self.plurality_winner = ''

    def __str__(self):
        '''
        The __str__ method returns a string representation 
        of the Plurality object winner.
        If there is no Plurality winner, the method returns
        'No Plurality Winner'.
        Parameters:
            self: a Plurality object
        Returns:
            msg: a string representing the Plurality object
        '''
        
        if self.plurality_winner:
            return self.plurality_winner
        else:
            return "No Plurality Winner."
             
        
    def determine_winner(self, data):
        '''
        The determine_winner method determines the Plurality winner.
        The Plurality winner is the candidate with the most #1 choice votes.
        If there is a tie, the method sets the Plurality winner to 
        an empty string.
        Parameters:
            data: VotingData object
        Returns:
            None
        '''
        votes = data.votes
        super().determine_winner(data)
        self.plurality_winner = self.majority_winner
        if self.plurality_winner:
            return 
        total_votes = {}
        for candidate in votes[0]:
            total_votes[candidate] = 0

        for vote in votes:
            total_votes[vote[0]] += 1
        ranked = []
        for candidate, num_of_votes in total_votes.items():
            ranked.append([num_of_votes, candidate])
        ranked.sort(reverse=True)
        if ranked[0][0] == ranked[1][0]:
            self.plurality_winner = ''
        else:
            self.plurality_winner = ranked[0][1]    

def main():
    '''
    The main function reads in voting data from a file and determines
    the winner of the election using the Plurality voting method.
    '''
    print('Plurality Voting Method')
    voting_data = VotingData()
    print(voting_data.num_of_votes)
    voting_data.print_percents()

    plurality = Plurality()
    print(f'Majority Winner: {plurality.majority_winner}')
    print(f'Plurality Winner: {plurality.plurality_winner}')
    
    plurality.determine_winner(voting_data)
    print(plurality)
    print(f'Majority Winner: {plurality.majority_winner}')
    print(f'Plurality Winner: {plurality.plurality_winner}')


if __name__ == '__main__':
    main()