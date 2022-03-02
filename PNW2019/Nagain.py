#COMPLETED
vars = [int(i) for i in input().split()]

R = vars[0]
C = vars[1]
A = vars[2] #how many vertical rectangles
B = vars[3] #how many horizontal rectangles
print(A,B)
ai = [] #height of rows
bj = [] #width of columns 

for i in range(A):
    ai.append(int(input()))

for i in range(B):
    bj.append(int(input()))

#for a row I go bj width. Then I switch colors
#when I go down a row if R was even then B W B W
black = True
grid = []
for i in range(A):
    for r in range(ai[i]):
        row = ""
        for j in range(B):
            if black:
                row += "B" * bj[j]
            else:
                row += "W" * bj[j]
            black = not black
        print(row)
    if B % 2 == 0: #odd columns
        black = not black

