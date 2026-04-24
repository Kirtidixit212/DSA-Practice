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
