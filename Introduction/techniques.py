#------------------- Simple Techniques that are useful --------------------
from pprint import pprint
from operator import itemgetter
from collections import defaultdict, Counter
#-- Comparisons
myTuple = (5,7,8,9,10,1,3)
largest_number = max(((myTuple[i],i) for i, _ in enumerate(myTuple)))
# print(largest_number)

myList = [("a",1),("b",5),("c",8),("d",2)]
myList.sort(key=itemgetter(1))
# print(myList)

myList = list("Mississippi".lower())
frequency_dict = defaultdict(int)
for letter in myList:
    frequency_dict[letter] += 1
# pprint(frequency_dict)

# pprint(Counter(myList).most_common(2))

def letter_frequeny(sentence):
    d = {} 
    for letter in sentence:
        frequency = d.setdefault(letter,0)
        d[letter] = frequency + 1
    return d

pprint(letter_frequeny("mississippi"))
