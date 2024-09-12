'''
The Condorcet class inherits from the Majority class.
The Condorcet class has the following attributes:
    condoret_winner: a string representing the Condorcet winner
    wins: a dictionary with the candidate as the key and the number of wins as the value
    
The Condorcet class has the following methods:
    __init__: initializes the Condorcet object
    __str__: returns a string representation of the Condorcet object
    remove_candidates: removes candidates from the votes
    print_wins: prints the head to head wins
    determine_winner: determines the Condorcet winner
'''

from majority import Majority
from voting_data import VotingData


class Condorcet(Majority):
    def __init__(self):
        '''
        The __init__ method initializes the Condorcet object.
        The Condorcet object inherits from the Majority object.
        The Condorcet object has the following attributes:
            condoret_winner: a string representing the Condorcet winner
            wins: a dictionary with the candidate as the key and the 
                  number of wins as the value
        Parameters:
            self - a Condorcet object
        Returns:
            None
        '''
        super().__init__()
        self.condoret_winner = ''
        self.wins = {}

    def __str__(self):
        '''
        The __str__ method returns a string representation
        of the Condorcet object winner.
        If there is no Condorcet winner, the method returns
        'No Condorcet Winner'.
        If there is a Condorcet winner, the method returns
        'The Condorcet Winner:\n' followed by the Condorcet winner.
        Parameters:
            self - a Condorcet object
        Returns:
            msg - a string representing the Condorcet object
        '''
        if self.condoret_winner:
            return f'The Condorcet Winner:\n{self.condoret_winner}\n'
        return 'No Condorcet Winner\n'
        
    def remove_candidates(self, votes, candidates):
        '''
        The remove_candidates method removes candidates from the votes.
        Parameters:
            votes: a list of lists of strings
            candidates: a list of strings that contains the 
                        two candidate names to keep
                        (so you should remove all other candidates)
        Returns:
            None
        '''
        
        for vote in votes:
            vote[:] = [cand for cand in vote if cand in candidates]
                

    def print_wins(self):
        
        '''
        The print_wins method prints the head to head wins.
        Make sure to print the candidates in descending order of wins.
        In the format:
        Candidate    : Wins
        ---------------------
        candidate1   : wins
        candidate2   : wins
        ...

        Parameters:
            self - a Condorcet object
        Returns:
            None
        '''
       
        
        
                    
        
        self.wins_sorted = sorted(self.wins, key=self.wins.get, reverse = True)
        print('One To One Wins: ')
        for r in self.wins_sorted:
            print(str(r) + '\t' + ':' + str(self.wins[r]))
        
        
        
            
            
        

        
    def determine_winner(self, data):
        '''
        The determine_winner method determines the Condorcet winner.
        To determine the Condorcet winner, the method compares each
        candidate to every other candidate. The method determines
        the winner of each head to head comparison. The candidate
        wins all their head to head comparisons is the Condorcet winner.
        If there is no Condorcet winner, the method sets the
        Condorcet winner to an empty string.
        Parameters:
            data: VotingData object
        Returns:
            None
        '''
 
        candidates = data.candidates
        votes = data.votes
        for name in candidates:
            self.wins[name] = 0
        original_votes = []
        for i in range(len(votes)):
            original_votes.append(votes[i].copy())
        for i in range(len(candidates)):
            for j in range(i+1, len(candidates)):
                self.remove_candidates(votes, [candidates[i], candidates[j]])
                super().determine_winner(data)
                self.condoret_winner = self.majority_winner
                if not self.condoret_winner:
                    print('No Condoret Winner')
                    return None
                self.wins[self.condoret_winner] += 1
                print(f'{candidates[i]} vs {candidates[j]}')
                print(f'{self.condoret_winner} wins: {self.wins[self.condoret_winner]}\n')
                for b in range(len(original_votes)):
                    votes[b] = original_votes[b].copy()
        for b in range(len(original_votes)):
            votes[b] = original_votes[b].copy()
        for candidate, num_of_wins in self.wins.items():
            winning_amount = len(self.wins) - 1
            if num_of_wins == winning_amount:
                self.condoret_winner = candidate
        return None
