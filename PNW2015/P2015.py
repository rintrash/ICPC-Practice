#COMPLETED
string = input()

#so i get all the unique ones put it into an array. Add counts. Then sort. Then erase
unique = []
count = []

for c in string: 
    if c not in unique:
        unique.append(c)
        count.append(1)
    else:
        count[unique.index(c)] += 1

count = sorted(count)

erase_count = 0
while len(count) > 2:
    erase_count += count.pop(0)

print(erase_count)