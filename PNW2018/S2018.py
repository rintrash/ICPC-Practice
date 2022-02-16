#COMPLETE 
#s = [int(i) for i in input()]
s = [int(i) for i in "3 10".split()]
cash = s[0] #cashiers
cust = s[1] #customers
customers = [int(i) for i in "406 424 87 888 871 915 516 81 275 578".split()]

pos = [0,0,0]
output = ""
#so we go in cash's first. While empty fill. Subtract by one 

while len(customers) != 0: 
    for i in range(len(pos)):
        if pos[i] == 0:
            pos[i] = customers[0] #if empty spot, take next customer
            customers.pop(0)
            output += str(i + 1) + " "
        pos[i] -= 1

print(output)
    