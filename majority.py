'''
The Majority class is used to determine the winner of an 
election using the majority voting method (one candidate
receives more than 50% of the votes). 

The Majority class has the following attributes:
    majority_winner: a string representing the majority winner
The Majority class has the following methods:
    __init__: initializes the Majority object
    __str__: returns a string representation of the Majority object
    determine_winner: determines the winner of the election
'''

class Majority:
    def __init__(self):
        '''
        The __init__ method initializes the majority_winner
        attribute to an empty string.
        Parameters:
            self - a Majority object
        Returns:
            None
        '''
        
        self.majority_winner = ''

    def __str__(self):
        '''
        The __str__ method returns a string representation of the
        majority_winner attribute. If there is a majority winner,
        the string will contain the majority winner. If there is
        no majority winner, the string will contain 'No Majority Winner'.
        Parameters:
            self - a Majority object
        Returns:
            msg: a string representing the Majority object
        '''
        if self.majority_winner:
            return 'Majority Winner: \n'+ self.majority_winner
        return "No Majority Winner"
  
        
    def determine_winner(self, data):
        '''
        The determine_winner method determines the winner of the election
        using the majority voting method. If a candidate receives more than
        50% of the votes, that candidate is the Majority winner. If no candidate
        receives more than 50% of the votes, there is no Majority winner.
        Parameters:
            data (VotingData): VotingData object that contains the voting data
        Returns:
            NYou will need to write the following functions: __init__, __str__, and determine_winner. The find_lowest function is complete and you should not change the code. The details for the InstantRunOff functions are outlined in the instant_run_off.py file.
Once you have correctly written __init__, __str__, and determine_winner, created a VotingData Object, created an InstantRunOff object, called the determine_winner function on the InstantRunOff object, and printed the InstantRunOff object, the output to the shell should be the following:one
        '''
        
        counts_dict = {}
        
        total_votes = len(data.votes)
        
        
        for vote in data.votes:
            candidate = vote[0]
            if candidate in counts_dict:
                counts_dict[candidate] += 1
            else:
                counts_dict[candidate] = 1
                
                
        for candidate, vote in counts_dict.items():
            if vote > total_votes / 2:
                self.majority_winner = candidate
                
            
                
        
        
        
    
        
  