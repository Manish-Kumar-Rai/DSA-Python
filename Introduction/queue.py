# --------------- Queue Implementation ---------------

"""
Implement a Queue using two stacks. One stack corresponds to the head of the queue
for extraction and the other corresponds to the tail for insertion.Once the head stack is empty,it is swapped with the tail stack(swapped).
The operator __len__ uses len(q) to recover the number of elements in the queue q, and then if q can be used to test if q is non-empty, in constant time.
"""

class OurQueue:
    def __init__(self):
        self.in_stack = []   #tail
        self.out_stack = []  #head

    def __len__(self):
        return len(self.out_stack) + len(self.in_stack)
    
    def push(self,value):
        self.in_stack.append(value)

    def pop(self):
        if not self.out_stack:        #head is empty
        #in_stack is assign to out_stack in reverse order
        #as in in_stack(order is oldest to newest)
        #but in out_stack(order will be newest to oldest)
        #so that oldest will be pop out
            self.out_stack = self.in_stack[::-1]
            self.in_stack = []
        return self.out_stack.pop()
    
    def __repr__(self):
        return f"{self.out_stack[::-1] + self.in_stack}"
    
q = OurQueue()
q.push(4)
q.push(6)
q.push(10)
print(q)
q.pop()
print(q)
q.pop()
print(q)
q.push(5)
print(q)