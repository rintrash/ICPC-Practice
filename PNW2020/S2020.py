#IDK
#so the majority same means that the class got it right
#so I could assign a value for each T or F 
#make a maximizing thing 

#creates tests with different solutions
import datetime
import itertools
from math import factorial

def createTests(numQs):
    #create all permutations of T F 
    perms = list(itertools.product('10',repeat = numQs))
    for j in range(len(perms)):
        perms[j] = [int(i) for i in perms[j]]
    
    return perms

def runSimulations(tests):
    simulation = []
    for i in range(len(perms)): 
        simulation.append([0 for i in range(len(tests))])
        for j in range(len(tests)):
            if tests[j] == perms[i][j]:
                simulation[i][j] += 1
    return simulation
#input = [int(i) for i in input().split()]
#numTests = input[0]
#numQs = input[1]
start = datetime.datetime.now()

numTests = 5
numQs = 4
perms = createTests(numQs)

#now I have all the permutations so I can find which one creates the largest min 
tests = []
for i in range(numTests):
    tests.append(input())

end = datetime.datetime.now()
simulation = runSimulations(tests) #list of the results for each permutation
print(start - end)

print(simulation)
#for sim in simulation:
    #min(sim)

