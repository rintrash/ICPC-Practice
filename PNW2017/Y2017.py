#inpt = [int(i) for i in input().split()]

k = 31#inpt[0] #days for one painter to finish
p = 41#inpt[1] #penalty
x = 59#inpt[2] #pay per painter

#find minimum cost 
#so if p > x 

paint = 2
curr = k * p + x 
next = (k / paint) * p + x * paint
print(curr, next)
while curr >= next: 
    curr = next 
    paint += 1
    next = k / paint * p + x * paint

value = round(curr,3)
print(f'{value:.3f}')



#k / painters * p + x * painters 
#idk