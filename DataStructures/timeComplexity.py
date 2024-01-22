#--------------------- Measuring Time Complexity-----------
import time
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

timeComplexity.timeToExecute(printNumberSeries,1000)