#COMPLETE: Had to look at solution

#gets all possible combinations of plate weights
from itertools import chain, combinations
def powerSet(wts):
    return chain.from_iterable(combinations(wts, r) for r in range(len(wts) + 1))
 
 #scanner stuff
str = input().split()
barbells = int(str[0])
plates = int(str[1])
str = input().split()
barbellWts = [int(i) for i in str]
str = input().split()
plateWts = [int(i) for i in str]

duplicate_sums = []
for i in range(plates):
    right = set(powerSet(plateWts[i:]))  #ensures they are not taking the same numbers 
    left = set(powerSet(plateWts[:i]))
    for leftCombos in left:
        for rightCombos in right:
            if sum(leftCombos) == sum(rightCombos):
                duplicate_sums.append(sum(leftCombos) * 2) #doubled for plates on each side

sumSet = set()
for b in barbellWts:
    for s in duplicate_sums:
        sumSet.add(b + s)

print(sorted(sumSet))       
