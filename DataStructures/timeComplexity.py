#--------------------- Measuring Time Complexity-----------
import time
import sys
import ctypes
from random import randint
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


# ----------- Crearting a List Class -------------------------

class MyList:
    def __init__(self):
        self.size = 1
        self.n = 0
        #Create a C type array with size self.size
        self.A = self.__create_array(self.size)

    def __len__(self):
        return self.n
    
    def __create_array(self,capacity):
        #Creates a C type array(static, referenecial) with size capacity
        return (capacity*ctypes.py_object)()
    
    def append(self,item):
        if self.n == self.size:
            #resizing
            self.__resize(self.size*2)
        #append
        self.A[self.n] = item
        self.n += 1
    
    def __resize(self,new_capacity):
        #Create an array with size new capacity
        B = self.__create_array(new_capacity)
        self.size = new_capacity
        #Copy content of A in B
        for i in range(self.n):
            B[i] = self.A[i]
        #Reassign self.A
        self.A = B

    def __str__(self):
        #print the content of an Array
        result = ""
        for i in range(self.n):
            result = result + str(self.A[i]) + ","
        return "[" + result[:-1] + "]"
    
    def __getitem__(self,index):
        try:
            if 0 <= index < self.n:
                return self.A[index]
            else:
                raise IndexError("Index out of range")
        except IndexError as e:
            print(e.args[0])

    def pop(self):
        if self.n == 0:
            return "Empty List."
        else:
            self.n -= 1
            return self.A[self.n]
    
    def clear(self):
        self.n = 0
        self.size = 1

    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return None
    
    def insert(self,pos,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        
        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n += 1

    def __delitem__(self,pos):
        if 0 <= pos < self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]
            self.n -= 1

    def remove(self,item):
        if i := self.find(item):
            self.__delitem__(i)
        else:
            print("Item not found")

    def min(self):
        min = self.A[0]
        for i in range(1,self.n):
            if self.A[i] < min:
                min = self.A[i]
        return min
    
    def max(self):
        max = 0
        for i in range(self.n):
            if max < self.A[i]:
                max = self.A[i]
        return max
    
    def sum(self):
        sum = 0
        for i in range(self.n):
            sum += self.A[i]
        return sum

L = MyList()

for i in "Manish Kumar Rai".split():
    L.append(i)

# print(f"List: {L}, size: {L.size}")
# print(L.pop())
# print(L.pop())
# print(L.pop())
# print(L.pop())
# L.clear()
# L.insert(1,"Vikas")
# print(L)
# del L[1]
# print(L)
# L.remove("Kumai")
# print(L)

L1 = MyList()
L1.append(35)
L1.append(48)
L1.append(56)
L1.append(91)
L1.append(23)

# print(L1)
# print(f"min: {L1.min()}")
# print(f"max: {L1.max()}")
# print(f"sum: {L1.sum()}")

#----------------------- Linked List ----------------------
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        # No. of nodes in linked list
        self.n = 0

    def __len__(self):
        return self.n
    
    def appendLeft(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.n += 1
            return
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.n += 1
            return
        
        self.tail.next = new_node
        self.tail = new_node
        self.n += 1

    def __str__(self):
        if self.head == None:
            return "Empty linked list."
        current_node = self.head
        result = ""
        while current_node != None:
            result = result +  str(current_node.data) + "->"
            current_node = current_node.next
        return result[:-2]


    def insert_after(self,after,data):
        new_node = Node(data)
        current_node = self.head
        while current_node != None:
            if current_node.data == after:
                break
            current_node = current_node.next
                
        if current_node != None:
            new_node.next = current_node.next
            current_node.next = new_node
            self.n +=1
        else:
            return "Item not found"

    def clear(self):
        self.head = None
        self.tail = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            return "Empty list."
        self.head = self.head.next
        self.n -= 1

    def pop(self):

        if self.head == None:
            return "Empty List"
        
        current_node = self.head

        # if Linked list contains only one item
        if current_node.next == None:
            self.tail = None
            return self.delete_head()

        while current_node.next.next != None:
            current_node = current_node.next

        # current_node is 2nd last node
        item = current_node.next.data
        current_node.next = None
        self.tail = current_node
        self.n -= 1
        return item
    
    def remove(self,value):
        if self.head == None:
            return "Empty List"
        
        if self.head.data == value:
            return self.delete_head()
        
        current_node = self.head
        
        while current_node.next != None:
            if current_node.next.data == value:
                break
            current_node = current_node.next
        
        if current_node.next == None:
            return "Item Not Found."
        else:
            current_node.next = current_node.next.next
            self.n -= 1

    def search(self,item):
        if self.head == None:
            return "Empty List"
        
        current_node = self.head
        pos = 0

        while current_node != None:
            if current_node.data == item:
                return pos
            current_node = current_node.next
            pos += 1

        return "Item Not Found"
    
    def __getitem__(self,index):
        current_node = self.head
        pos = 0

        while current_node != None:
            if pos == index:
                return current_node.data
            current_node = current_node.next
            pos += 1
        
        return "IndexError"
        
linkedList = LinkedList()
# linkedList.appendLeft("Rai")
# linkedList.appendLeft("Kumar")
# linkedList.appendLeft("Manish")
# linkedList.append("Manish")
# linkedList.append("Kumar")
# linkedList.append("Rai")
# print(len(linkedList))
# linkedList.append(1998)
# linkedList.insert_after("Kumar","Inserted")
# print(linkedList.insert_after("1231","oadj"))
# linkedList.clear()
# linkedList.delete_head()
# print(linkedList.pop())
# print(linkedList.pop())
# print(linkedList.pop())
# print(linkedList.pop())
# linkedList.append(2024)
# print(linkedList.remove("Manish"))
# print(linkedList.remove("Kumar"))
# print(linkedList.remove("Rai"))
# print(linkedList)
# print(len(linkedList))
# print(f"position: {linkedList.search('Kumar')}")
# print(linkedList[1])


L = LinkedList()
for i in range(1,6):
    L.append(i)

# print(L)

# Question linked list
def fun(head):
    if (head == None):
        return
    if head.next.next != None:
        print(head.data,end=" ")
        fun(head.next)
    print(head.data,end=" ")

# fun(L.head)
    
def replace_max_value_node(head,value):
    max = 0
    max_node = None
    if head == None:
        return "Empty List"
    current_node = head
    while current_node != None:
        if current_node.data >= max:
            max = current_node.data
            max_node = current_node
        current_node = current_node.next

    max_node.data = value

# replace_max_value_node(L.head,"Max")    
# print(L)

def odd_sum(head):
    sum = 0
    current_node = head
    pos = 0
    while current_node != None:
        if pos % 2 != 0:
            sum += current_node.data
        current_node = current_node.next
        pos += 1
    
    return sum

# print(odd_sum(L.head))

def reverse_ll(list):
    curr = list.head
    prev = None
    while curr != None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    list.head = prev


# reverse_ll(L)
# print(L)

string_ll = LinkedList()
for i in "An*/apple*a/day//keeps/*a//doctor*Away":
    string_ll.append(i)

print(string_ll)


