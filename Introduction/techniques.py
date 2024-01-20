#------------------- Simple Techniques that are useful --------------------
from pprint import pprint
from operator import itemgetter
from collections import defaultdict, Counter
from random import randint
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

nb_occurrence = Counter(myList)
# pprint(nb_occurrence.most_common(2))

def letter_frequeny(sentence):
    d = {} 
    for letter in sentence:
        frequency = d.setdefault(letter,0)
        d[letter] = frequency + 1
    return d

# pprint(letter_frequeny("mississippi"))

def majority(sentence):
    d = dict()
    for letter in sentence:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    return d

frequency_dict1 = majority('Mississippi')

val_1max,arg_1max = min((-frequency_dict1[letter],letter) for letter in frequency_dict1)
# print(val_1max,arg_1max)

#-------- Sorting

# L = list(set([randint(50,100) for _ in range(15)]))

def closest_value(list):
    list.sort()
    print(f"Sorted List: {list}")
    closest = [(list[i] - list[i-1],i) for i in range(1,len(list))]
    print(closest)
    val, arg = min(closest)
    return (val,arg)

# print(closest_value(L))

# ------ Sweep Line-------------------

"""
Numerous problem in geometry can be solved with sweep line technique, including many problems concerning intervals. 
"""
arrival_point = [randint(1,5) for _ in range(5)]
dept_point = [randint(6,12) for _ in range(5)]
myIntervals = [(arr,dept) for arr, dept in zip(arrival_point,dept_point)]
pprint(myIntervals)

def max_interval_intersec(intervals):
    B = (
        [(arr,+1) for arr,_ in intervals]+
        [(dept,-1) for _, dept in intervals]
    )
    B.sort()
    max_customer = 0
    best = (max_customer,None)
    for time,events in B:
        max_customer += events
        if best[0] < max_customer:
            best = (max_customer,time)
    return best
pprint(max_interval_intersec(myIntervals))