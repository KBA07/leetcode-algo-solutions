"""
bool knows (a,b) weather a knows b
people (0, N-1)
"""

# API bool knows(a,b) whether a knows b or not
def knows(a, b):
    pass

def findCelebrity(N):

    celebrity_candidate = 0

    for people in range(1, N): # Since celebrity is known by N-1 people hence after this loop we will have a candidate
        if knows(celebrity_candidate, people):
            celebrity_candidate = people
    
    for people in range(N):
        
        if celebrity_candidate != people and knows(celebrity_candidate, people) and not knows(people, celebrity_candidate):
            return -1
    
    return celebrity_candidate
