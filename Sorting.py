# BUBBLE SORT
# input   arr=[8,9,2,1,3,7]
# output    arr=[1,2,3,7,8,9]
def bubbleSort(arr):

    for i in range(len(arr)):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped :
            break
    return arr   


#SELECTION SORT
def selectionSort(nums):
    n = len(nums)
    for i in range(n-1):
        min = i
        for j in range(i + 1,n):
            if nums[j] < nums[min]:
                min = j
        nums[min],nums[i] = nums[i],nums[min]
    return nums
    
# INSERTION SORT
def insertion_sort(nums):
    n = len(nums)

    for i in range(1,n):
        curr = nums[i]
        prev = i - 1
        
        while prev >= 0 and nums[prev] > curr:
            arr[prev+1] = arr[prev]
            prev -= 1
        nums[prev +1] = curr
    return num        
