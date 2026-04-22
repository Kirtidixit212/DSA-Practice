# Move zeros Problem
input:  arr = [1,0,2,3,0,4,0,1]
output:  arr = [1,2,3,4,1,0,0,0]

def movezeros(arr):
    j = -1  # ready to be a pointer to the first zero 
    # let's find first zero
    for i in range(len(arr)):
        if arr[i] == 0:
            j = i
            break
    # but if there is no zero ,return
    if j == -1:
        return arr
    # when zero is found
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i],arr[j] = arr[j],arr[i] #swapped
            j += 1
    return arr      
    
    
    
    
    
    
# Remove Duplicates Problem
# input : nums = [0,1,0,3,7,5,7]
def remove_duplicate(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1            




