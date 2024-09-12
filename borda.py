'''
The Borda voting method is a ranked voting method that assigns 
points to candidates based on their rank. The candidate with 
the highest number of points wins the election.

Note that the Borda class is NOT a subclass.
The Borda class has the following attributes:
    borda_winner: a string representing the Borda winner
    points: a dictionary with the candidate as the key and the 
            number of points as the value
The Borda class has the following methods:
    __init__: initializes the Borda object
    __str__: returns a string representation of the Borda object
    print_points: prints the points for each candidate
    determine_winner: determines the Borda winner
'''

class Borda:
    
    def __init__(self):
        '''
Initializes the self.borda winner object to an empty string and self.points dictionary to an empty dictionary

'''
        
        self.borda_winner = ''
        
        self.points = {}
        
    def __str__(self):
        '''
This is the string representation of the self.borda_winner object and returns the winner if there is one
and returs 'No Borda Winner' if there isn't one

'''
        
        if self.borda_winner:
            return "Borda Winner: " + str(self.borda_winner)
        else:
            return "No Borda Winner"
        
    def print_points(self):
        '''
This prints the format in which it is required. It tells us how many points each candidate gets based on their
rank and then prints each candidate with their corresponding points by extracting them from self.points
dictionary.

'''
        
        print('Borda Voting Method')
        num_candidates = 5
        for i in range(num_candidates, 1, -1):
            print(f"{i - 1} points for {num_candidates - (i - 1)}{'st' if num_candidates - (i - 1) == 1 else 'nd' if num_candidates - (i - 1) == 2 else 'rd' if num_candidates - (i - 1) == 3 else 'th'} ranked vote")
        print('The candidate with the highest number of points win.\n')
        print('Candidate   : Points\n-------------') 
        for key, value in self.points.items():
            print(f"{key}: {value}")
        
        
        
       
  
            
    def determine_winner(self, votes):
        '''
This determines the winner. It assisgns the points for each candidate based on their rank in the second for loop
and then extracts the candidate with the max points to be the borda winner.

'''
       
        for vote in votes:
            for rank, candidate in enumerate(vote):
                candidate = candidate.strip()
                if candidate in self.points:
                    self.points[candidate] += len(vote) - rank - 1
                else:
                    self.points[candidate] = len(vote) - rank - 1
 
                
        for key, value in self.points.items():
           print(key + ": " + str(value))
                
        self.borda_winner = max(self.points, key=self.points.get)
        print("\nBorda Winner: \n" + str(self.borda_winner))
        
        
        
        
            

        
        
        
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
                
        
    
        
        
            
        
        
        
        


        
        
