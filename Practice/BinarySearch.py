#So my goal is to search for a number quickly 
#the list has to already be sorted
def binarySearch(nums, l, h, goal):
    midIndex = (l + h) // 2  #1 2 3 4 5 6
    midNum = nums[midIndex]
    
    while(l <= h):
        if midNum == goal:
            return midIndex
        elif goal < midNum:
            return binarySearch(nums, l, midIndex - 1, goal)
        else:
            return binarySearch(nums, midIndex + 1, h, goal)
    
    return -1

nums = [1,2,3,4,5,6]

print(binarySearch(nums, 0, len(nums) - 1, -1))
