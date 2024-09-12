'''
Project 3 - Voting Methods - Spring 2024  
Author: Aayush Narang (anarang27)

I have neither given or received unauthorized assistance on this assignment.
Signed:  Aayush Narang
'''


'''
The VotingData class is a class that reads in data from a file and 
stores the data in a list of lists.
The list of lists contains the votes of the candidates.
The VotingData class also stores the number of votes and the candidates.

The VotingData class has the following attributes:
    num_of_votes: an integer representing the number of votes
    votes: a list of lists of strings representing the votes
    candidates: a list of strings representing the candidates
The VotingData class has the following methods:
    __init__: initializes the VotingData object
    __str__: returns a string representation of the VotingData object
    get_data: reads in the data from a file and stores the data
    print_percents: prints the percentage of votes for each candidate
'''

class VotingData:
    
    def __init__(self):
        '''
        The __init__ method initializes the VotingData object.
        Note that you should call the get_data function in the 
        __init__ method so that the data is assigned to the 
        instance variable votes when the VotingData object 
        created.
        The VotingData object has the following attributes:
            num_of_votes: an integer representing the number of votes
                          set the value to 0
            votes: a list of lists of strings representing the votes
                   set the value to an empty list
            candidates: a list of strings representing the candidates
                        set the value to an empty list

        Parameters:
            self - a VotingData object
        Returns:
            None
        '''
        
        self.num_of_votes = 0
        self.votes = []
        self.candidates = []
        self.get_data()
        

    def __str__(self):
        '''
        The __str__ method returns a string representation of the 
        VotingData object.
        The string representation includes the total number of 
        votes and all the candidates.
        The msg is in the format:
        Total Votes: num_of_votes
        Below are all the Candidates:
        candidate1
        candidate2
        ...

        Parameters:
            self - a VotingData object
        Returns:
            msg: a string representing the VotingData object
        '''
        
        msg = '\nTotal Votes: ' + str(self.num_of_votes) + '\n'
        msg += '\nBelow are all the candidates: \n'
        msg += '\n'.join(self.candidates)
        
        return msg     
    
   
    def get_data(self):
        '''
        The get_data method reads in the data from the file named project3_data.txt
          and stores the data in the votes attribute.
        The candidates are stored in the candidates attribute.
        Note: there should be no duplicates in the candidates attribute.

        Parameters:
            self - a VotingData object
        Returns:
            None
        '''
        with open('project3_data.txt', 'r') as file:
            
            for line in file:
                data = [name.strip() for name in line.split(',')]
                self.votes.append(data)
                self.num_of_votes += 1
                
            for vote in data:
                candidate = vote.strip()
                if candidate not in self.candidates:
                    self.candidates.append(candidate)
                
     
    def print_percents(self):
        '''
        The print_percents method prints the percentage of votes 
        for the #1 choice for each candidate.
        Make sure to print the candidates in descending order of votes.
        The method prints the percentage of votes in the format:
        number of #1 choice votes  percent candidate
        number of #1 choice votes  percent candidate
        number of #1 choice votes  percent candidate
        ...

        Parameters:
            self - a VotingData object
        Returns:
            None
        '''
        
        counts_dict = {}
        
        for vote in self.votes:
            candidate = vote[0].strip()
            if candidate in counts_dict:
                counts_dict[candidate] += 1
            else:
                counts_dict[candidate] = 1
                
                
        total_votes = len(self.votes)
        
        print('Voting Methods')
        for candidate in sorted(counts_dict, key=counts_dict.get, reverse=True):
            
            num_votes = counts_dict[candidate]
            
            percent = ((num_votes / total_votes) * 100)
            
            percent_rounded = round(percent, 1)
            
            print(str(num_votes) + "  " + str(percent_rounded) + "%  " + candidate)
            
    
            
            


        
        
        
        
                          
                
        
        
        
        
        