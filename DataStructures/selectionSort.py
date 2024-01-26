#---------------------- Selection Sort-----------------------
myList = [5,7,6,4,3]

def selection_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    print(arr)

selection_sort(myList)