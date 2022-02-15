s = input() 

odd = True

for c in range(0, len(s) - 1): #0 to ?
  #print(c)
  curr = s[c]
  nxt = s[c + 1]
  if curr is nxt:
    odd = False
    break

if odd: 
  print("Odd.")
else:
  print("or not")
