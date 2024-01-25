# find an array is sorted or not

myList = [5,4,8,3,1,9,7]

myListSorted = sorted(myList)[::-1]
print(myList)
print(myListSorted)

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

print(f"myList: {is_sorted(myList)}")
print(f"myListSorted: {is_sorted(myListSorted)}")