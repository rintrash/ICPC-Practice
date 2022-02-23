import datetime
start = datetime.datetime.now()
string = "lurabvxewhjmzyqcgkpisdntfo"
output = ""
for c in string:
    if string.count(c) > 1:
        output = "0"
        break
    else:
        output = "1"
        continue

print(output)
end = datetime.datetime.now()
print(end - start, "seconds")
    