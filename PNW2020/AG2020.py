import datetime



tot = int(input())

nums = []
for i in range(tot):
    nums.append(int(input()))

start = datetime.datetime.now()
totSum = sum(nums)
output = 0
for i in range(tot):
    current = nums[0]
    nums.pop(0) 
    if current == sum(nums):
        output = current
        break
    else:
        output = "BAD"
        nums.append(current)
print(output)

print(datetime.datetime.now() - start, "seconds")
