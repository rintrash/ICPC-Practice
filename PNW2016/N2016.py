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
print(plateWts)
#output different possible distinct weights
#find all sums of plateWts that are same 
#i need a set of some sort 

plateCombos = combinePlates(plateWts) 
#make dictionary of the key combos and sum values 
plate_dict = {}
print(plateCombos)
for c in plateCombos:
    sumWts = sum(c)
    if sumWts in plate_dict:
        plate_dict[sumWts] = [c, plate_dict[sumWts]]
    plate_dict[sum(c)] = c

print(plate_dict)

