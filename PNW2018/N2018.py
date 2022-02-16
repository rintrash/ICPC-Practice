#COMPLETE
fCorrect = 6
myAns = "TTTTTTTT"
fAns = "FFFFFFFF"
same = 0
diff = 0

for i in range(len(myAns)):
    if myAns[i] is fAns[i]:
        same += 1
    else:
        diff += 1

if(fCorrect > same):
    diff = diff - fCorrect + same 
max = min(fCorrect, same) + diff

print(max)

#so we should have a list of the same
#list of different 