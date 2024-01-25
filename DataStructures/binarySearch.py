#--------------------Binary Search---------------
from random import randint
from sys import stdin

myList = list(
    set(
        [randint(1,15) for _ in range(10)]
    )
)

myList.sort()
print(myList)

def binarySearch(arr,low,high,item):
    mid = (low + high)//2
    
    if low <= high:
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binarySearch(arr,low,mid-1,item)
        else:
            return binarySearch(arr,mid+1,high,item)
    else:
        return -1

item = int(stdin.readline())

print(binarySearch(myList,0,len(myList)-1,item))