#------------------------ Bubble Sort --------------------

myList = [45,54,56,91,93,99]

def bubble_sort(arr):
    counter = 0
    for i in range(len(arr)-1):
        flag = 0
        for j in range(len(arr)-1-i):
            counter += 1
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = 1

        if flag == 0:
            break
    
    print(counter)

    return arr

print(bubble_sort(myList))