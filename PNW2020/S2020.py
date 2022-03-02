#UNFINISHED
#so the majority same means that the class got it right
#so I could assign a value for each T or F 
#make a maximizing thing 

#creates tests with different solutions
import datetime
import itertools
from math import factorial

def createTests(numQs):
    #create all permutations of T F 
    perms = list(itertools.product('TF',repeat = numQs))
    return perms

start = datetime.datetime.now()

numTests = 3
numQs = 5
perms = createTests(numQs)

#now I have all the permutations so I can find which one creates the largest min 
tests = []
for i in range(numTests):
    tests.append(input())

end = datetime.datetime.now()


