num = int( input())
numS = str(num+1)

while ("0" in numS):
    num += 1
    numS = str(num)
  
print(numS)