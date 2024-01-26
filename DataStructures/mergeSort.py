#----------------------Merge Sort ----------


arr = [1,3,5,4,9,2,6,8]

def merged(a,b):
    i = 0
    j = 0
    arr = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr.append(a[i])
            i += 1
        else:
            arr.append(b[j])
            j += 1

    if i < len(a):
        for k in range(i,len(a)):
            arr.append(a[k])
    if j < len(b):
        for k in range(j,len(b)):
            arr.append(b[k])

    return arr



def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left_arr = merge_sort(left)
    right_arr = merge_sort(right)

    return merged(left_arr,right_arr)

# print(merge_sort(arr))

#---------------Optimized (in place sorting) -------------------

def merged2(left,right,arr):
    i=j=k=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return


def merge_sort2(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort2(left)
    merge_sort2(right)

    return merged2(left,right,arr)

arr2 = arr[:]
print(arr2)
merge_sort2(arr2)
print(arr2)