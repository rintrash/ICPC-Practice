from itertools import combinations
def combinePlates(wts):
        if(len(wts) == 0):
            return [[]]

        #could just add all combinations 
        
        combos = []
        for c in combinePlates(wts[1:]):  
           combos += [c, c+[wts[0]]]

        return combos
 
str = input().split()
barbells = int(str[0])
plates = int(str[1])

str = input().split()
barbellWts = [int(i) for i in str]
str = input().split()
plateWts = [int(i) for i in str]
#print(plateWts)
#output different possible distinct weights
#find all sums of plateWts that are same 
#i need a set of some sort 

plateCombos = combinePlates(plateWts) 
plateCombos = [sum(i) for i in plateCombos]

duplicate_sums = set()
print(plateCombos)
for s in plateCombos:
    if plateCombos.count(s) > 1:
        duplicate_sums.add(s)

print(duplicate_sums)

sumSet = set()
for b in barbellWts:
    for s in duplicate_sums:
        sumSet.add(b + s)

print(sumSet)       
