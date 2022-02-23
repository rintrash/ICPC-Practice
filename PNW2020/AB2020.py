string = "4 4"
judges = [int(i) for i in string.split()]

remaining = judges[0] - judges[1]

sum = 0
for i in range(judges[1]):
    sum += int(input())

max = (remaining * 3 + sum) / judges[0]
min = (remaining * -3 + sum) / judges[0]

print(min,max)
