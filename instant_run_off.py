'''
The Instant Run Off Class is a subclass of the Majority class.
The Instant Run Off Class inherits the attributes and methods 
of the Majority class.

The Instant Run Off Class has the following attributes:
    run_off_winner: a string representing the Instant Run Off winner
    
The Instant Run Off Class has the following methods:
    __init__: initializes the Instant Run Off object
    __str__: returns a string representation of the Instant Run Off object
    find_lowest: returns the candidate with the lowest number of votes
    determine_winner: determines the Instant Run Off winner

'''

from majority import Majority
from voting_data import VotingData

class InstantRunOff(Majority):
    def __init__(self):
        '''
        The __init__ method initializes the Instant Run Off object.
        The Instant Run Off object inherits from the Majority object.
        The Instant Run Off object has the following attributes:
            run_off_winner: a string representing the Instant Run Off winner
                            set the attribute to an empty string
        Parameters:
            self: an Instant Run Off object
        Returns:
            None
        '''
        super().__init__()
        self.run_off_winner = ''
        

    def __str__(self):
        '''
        The __str__ method returns a string representation
        of the Instant Run Off object winner.
        If there is no Instant Run Off winner, the method returns
        'No Instant Run Off Winner'.
        If there is an Instant Run Off winner, the method returns
        'The Instant Run Off Winner:\n' followed by the Instant Run Off winner.
        Parameters:
            self: an Instant Run Off object
        Returns:
            msg: a string representing the Instant Run Off object
        '''
        
        
        
        if self.run_off_winner:
            return 'The Instant Run Off Winner:\n' + self.run_off_winner
        return 'No Instant Run Off Winner.'
            
            
            
            
    
    def find_lowest(self, votes):
        '''
        The find_lowest method returns the candidate with the 
        lowest number of #1 choice votes.
        Parameters:
            votes: a list of lists of strings
        Returns:
            lowest_candidate: a string representing the 
              candidate with the lowest number of votes
        '''
        rankings = {}
        for vote in votes:
            if vote[0] not in rankings:
                rankings[vote[0]] = 1
            else:
                rankings[vote[0]] += 1
        lowest_cand = ''
        lowest_count = len(votes)
        for candidate in rankings:
            if rankings[candidate] < lowest_count:
                lowest_cand = candidate
                lowest_count = rankings[candidate]
        return lowest_cand
    
    
    def determine_winner(self, data):
        '''
        The determine_winner method determines the Instant Run Off winner.
        The Instant Run Off winner is determined by eliminating the candidate
        with the lowest number of votes. The process is repeated until
        a candidate receives more than 50% of the votes. If a candidate
        receives more than 50% of the votes, that candidate is the Instant
        Run Off winner.
        To allow you to have practice with you newly found love of inheritance,
        make sure you use the inherited determine_winner function from the 
        Marjority class. 
        If there is no Instant Run Off winner, the method sets the 
        Instant Run Off winner to an empty string.
        Parameters:
            data: VotingData object
        Returns:
            None
        '''                  
                    
        votes = [vote[:] for vote in data.votes]  
        candidates = set(candidate for vote in votes for candidate in vote)
        
        
        while not self.majority_winner:
            
            first_votes = {candidate: 0 for candidate in candidates}
            for vote in votes:
                if vote:
                    first_votes[vote[0]] += 1

        
            total_votes = sum(first_votes.values())
            for candidate, count in first_votes.items():
                if count > total_votes / 2:
                    self.run_off_winner = candidate
                return
            
            
            lowest_candidate = min(first_votes, key=first_votes.get)
            candidates.remove(lowest_candidate)
            votes = [[candidate for candidate in vote if candidate != lowest_candidate] for vote in votes]


            if len(candidates) == 1:
                self.run_off_winner = candidates.pop()
            
            

def main():
    print('The Instant Run Off Method')
    data = VotingData()
    runoff = InstantRunOff()
    runoff.determine_winner(data)
    print(runoff)

if __name__ == '__main__':
    main()
        
        
        