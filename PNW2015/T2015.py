#have to determine if right triangle and have the same numbers
def sameSides(t1, t2):
    for i in range(3):
        if t1[i] != t2[i]:
            return False
    return True

def isRight(t):
    if (t[0]**2 + t[1]**2) == t[2]**2: #pythagorean theorem
        return True
    else:
        return False  
t1 = sorted([int(i) for i in input().split()])
t2 = sorted([int(i) for i in input().split()])

if sameSides(t1, t2) and isRight(t1) and isRight(t2):
    print("YES")
else:
    print("NO")
