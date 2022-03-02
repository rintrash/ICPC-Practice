#so each character is 3 length, except the last one
#each unique is an extra point. so we can store this as a list. map?
#so it's 1 length, 2length, 3, 4, etc. 

string = "The quick brown dog jumps over the lazy fox."
string = string.lower()
score = (len(string) - 1) * 3
unique = []
for c in string:
    if c.isalpha():   
        if c not in unique:
            unique.append(c)
        score += unique.index(c) + 1
    print(score)

print(unique)
print(score)