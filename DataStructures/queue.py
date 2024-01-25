#---------------- Queues --------------------------

# Queue using list
    
class OurQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)
    
    def __str__(self):
        result = ""
        queue = self.out_stack[::-1] + self.in_stack
        for i in range(len(queue)):
            result += str(queue[i]) + "->"
        return result[:-2]
    
    def enqueue(self,item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            if not self.in_stack:
                return "Empty Queue."
            self.out_stack = self.in_stack[::-1]
            self.in_stack = []
        return self.out_stack.pop()
    
    def __getitem__(self,index):
        queue = self.out_stack[::-1] + self.in_stack
        return queue[index]
    

# queue = OurQueue()
# queue.enqueue("Manish")
# queue.enqueue("Kumar")
# queue.enqueue("Rai")
# print(queue)
# print(queue[1])
# print(len(queue))
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())


#Queue Using linked list
    
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class OurQueue2:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def __len__(self):
        return self.n
    
    def __str__(self):
        curr = self.head
        result = ""
        while curr != None:
            result += str(curr.data) + "->"
            curr = curr.next
        return result[:-2]
    
    def enqueue(self,data):
        node = Node(data)
        if self.tail == None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self.n += 1

    def dequeue(self):
        if self.head == None:
            return "Empty Queue"
        item = self.head.data
        self.head = self.head.next
        self.n -= 1
        return item
    
    def __getitem__(self,index):
        if self.head == None:
            return
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos += 1
    
# queue2 = OurQueue2()
# queue2.enqueue("Manish")
# queue2.enqueue("Kumar")
# queue2.enqueue("Rai")
# print(len(queue2))
# print(queue2)
# print(queue2[1])
# print(queue2.dequeue())
# print(len(queue2))
# print(queue2)
            

#Question on queues-------------

queue = OurQueue()

def fun(num):
    if num == 0:
        return 0
    else:
        queue.enqueue(num%10)
        res = fun(num//10)
        res = res*10 + queue.dequeue()
        return res
    
# print(fun(123))