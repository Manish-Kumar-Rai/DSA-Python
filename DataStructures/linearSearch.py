#--------------------- Linear Search------------------------
# Based on Brute force
from random import randint

myList = list(
    set(
        [randint(1,101) for _ in range(100)]
))

def linear_search(arr,item):
    for i in arr:
        if i == item:
            return True
    return False

print(linear_search(myList,55))