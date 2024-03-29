#------------------- Simple Techniques that are useful --------------------
from pprint import pprint
from operator import itemgetter
from collections import defaultdict, Counter
from random import randint
from sys import stdin
import time
from functools import lru_cache
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
# pprint(myIntervals)

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


# ----------- Greedy Algorithm----------------

#--Minimal Scalar Product
# x = list(map(int,stdin.readline().split()))
# y = list(map(int,stdin.readline().split()))

def min_scalar_product(x,y):
    x1 = sorted(x)
    y1 = sorted(y)
    return sum(x1[i] * y1[-i-1] for i in range(len(x1)))

# print(min_scalar_product(x,y))

#----------- Dynamic Progrramming------------------
"""
The idea is to store a few precious bits of information so as to not have to recompute them while solving
a problem, and then to reflect on how to astutely combine these bits.

"""

# Naive approach
def fibo_naive(n):
    if n <= 1:
        return n
    return fibo_naive(n-1) + fibo_naive(n-2)

# t1 = time.time()
# print(fibo_naive(35))
# print(f"Total Time: {time.time()-t1}")

#dynamic programming
def fibo_dp(n):
    mem = [0,1]
    for i in range(2,n+1):
        mem.append(mem[-1]+mem[-2])
    return mem[-1]

# t1 = time.time()
# print(fibo_dp(35))
# print(f"Total Time: {time.time()-t1}")

#dynamic + memmory reduce approach
def fibo_dp_mem(n):
    mem = [0,1]
    for i in range(2,n+1):
        mem[i%2] = mem[0] + mem[1]
    return mem[n%2]

# t1 = time.time()
# print(fibo_dp_mem(35))
# print(f"Total Time: {time.time()-t1}")

@lru_cache(maxsize=None)
def fibo_naive2(n):
    if n <= 1:
        return n
    return fibo_naive2(n-1) + fibo_naive2(n-2)

# t1 = time.time()
# print(fibo_naive2(35))
# print(f"Total Time: {time.time()-t1}")

#----------Encoding of sets by integers--------------

s1 = {0}    #Empty set
n = 2
s2 = {1<<n}  #represents:- (2^n)
s3 = {(1<<n)-1}  #represents:- (2^n) - 1
A = {1,2,3,4,5}   # Set A
B = {3,4,5,6,7}   # Set B
# print(f"logical or: {A|B}")
# print(f"logical and: {A&B}")
# print(f"exclusive or : {A^B}")
# print(f"test of inclusion: {A&B==A}. meaning A is not subset of B.")
# print(f"test of membership: {s2&A}")
# print(f"this expression equals 0 if A is empty: {min(A)}, -A&A")

myList = [2,3,4,5,1,6]

# Naive algorithm O(2^2n)
def three_partition(x):
    f = [0] * (1<<len(x))
    for i, _ in enumerate(x):
        for S in range(1<<i):
            f[S|(1<<i)] = f[S] + x[i]
    for A in range(1 << len(x)):
        for B in range(1 << len(x)):
            if A & B == 0 and f[A] == f[B] and 3 * f[A] == f[-1]:
                print(f[A],f[B],f[C := ((1<< len(x))-1)^A^B],f[-1])
                return (A, B, C)
    return None
# pprint(three_partition(myList))

#---------Binary Search----------------------


