#------------------- Monkey Sort ----------------
import random

def is_sorted(arr):
    first = arr[0]
    last = arr[-1]
    if first == last:
        return False
    elif first < last:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
    elif first > last:
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                return False
            
    return True

def monkey_sort(arr):

    while not is_sorted(arr):
        random.shuffle(arr)
        print(arr)
    
    return arr

myList = [4,7,3,9]
print(myList)
print("---------process start----------")
sortarr = monkey_sort(myList)
print("---------process end-------------")
print(sortarr)