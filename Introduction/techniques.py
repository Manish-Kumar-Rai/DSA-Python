#------------------- Simple Techniques that are useful --------------------
from pprint import pprint
from operator import itemgetter
#-- Comparisons
myTuple = (5,7,8,9,10,1,3)
largest_number = max(((myTuple[i],i) for i, _ in enumerate(myTuple)))
print(largest_number)

myList = [("a",1),("b",5),("c",8),("d",2)]
myList.sort(key=itemgetter(1))
print(myList)

