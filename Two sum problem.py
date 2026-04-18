# leetcode problem:1
# nums = [2,7,11,15]   ,target = 9   

def twosum(nums,target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return[hashmap[complement],i]
        hashmap[nums[i]] = i
    return[]     # if no solution   


   

        
