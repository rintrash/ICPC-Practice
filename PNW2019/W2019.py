#check row for same number -- easy 
#check column for same number -- eh
#check 3 in row 

def checkColumn(grid):
    column = []
    for j in range(len(grid)):
        for i in range(len(grid)):
            column.append(grid[i][j])
        white = 0
        black = 0
        for k in column:
            if k == "W":
                white += 1
            else:
                black += 1  
        if white != black or column.count("WWW") >= 1 or column.count("BBB") >= 1:
            return False
    return True 

def getGrid(grid):
    rows = int(input())

    for i in range(rows):
        white = 0
        black = 0
        grid.append(input())
        for j in grid[i]:
            if j == "W":
                white += 1
            else:
                black += 1
        #2print(white, black)
        if white != black or grid[i].count("WWW") >= 1 or grid[i].count("BBB") >= 1:
            return False
    return True

grid = []
if getGrid(grid) and checkColumn(grid): 
    print(1)
else:
    print(0)


