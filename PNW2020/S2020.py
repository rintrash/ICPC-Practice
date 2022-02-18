#COMPLETE?
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
    #for j in range(len(perms)):
        #perms[j] = [int(i) for i in perms[j]]
    
    return perms

def runSimulations(numQs):
    simulation = []
    for i in range(len(perms)): 
        simulation.append([0 for i in range(len(tests))])
        for j in range(numQs):
            for k in range(len(tests)):
                #print(test[j], perms[i][j])
                if tests[k][j] is perms[i][j]:
                    simulation[i][k] += 1
    return simulation

#input = [int(i) for i in input().split()]
#numTests = input[0]
#numQs = input[1]
start = datetime.datetime.now()

numTests = 3
numQs = 5
perms = createTests(numQs)

#now I have all the permutations so I can find which one creates the largest min 
tests = []
for i in range(numTests):
    tests.append(input())

end = datetime.datetime.now()
simulation = runSimulations(numQs) #list of the results for each permutation
maxmin = 0
for sim in simulation:
    if min(sim) > maxmin:
        maxmin = min(sim)
print(end - start)

print(maxmin)
#for sim in simulation:
    #min(sim)

