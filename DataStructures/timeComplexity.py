#--------------------- Measuring Time Complexity-----------
import time
import sys
# 1. Measuring time to execute
class TimeComplexity:
    def timeToExecute(self,fn,n):
        t1 = time.time()
        fn(n)
        print(f"Total Time: {time.time()-t1}")


timeComplexity = TimeComplexity()

def printNumberSeries(n):
    myList = []
    # for i in range(n):       #time = 0.001
    #     myList.append(str(i))
    i = 0
    while i < n:      #time = 0.001
        myList.append(str(i))
        i += 1 
    print(",".join(myList))

# timeComplexity.timeToExecute(printNumberSeries,1000)

def intToStr(n):    #O(log n)
    digits = "0123456789"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n%10] + result
        n //= 10    # when inputs divide , generally log case
    return result

# print(intToStr(5))

# log property :- input add, output multiply

#------------ List ----------------------
# To Show list is dynamic in python
L = []

# for i in range(1,101):
#     print(f"value: {i}, size: {sys.getsizeof(L)}")
#     L.append(i)