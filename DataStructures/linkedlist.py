
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
        
# linkedList = LinkedList()
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
for i in "An*/apple*a/day//keeps/*a//doctor*/away":
    string_ll.append(i)

# print(string_ll)

string_ll2 = LinkedList()
for i in "Hello,*/i'm//manish**rai.":
    string_ll2.append(i)

# print(string_ll2)

def string_beauty(list):
    curr = list.head
    while curr != None:
        if curr.data == "*" or curr.data == "/":
            if curr.next.data == "*" or curr.next.data == "/":
                curr.data = " "
                curr.next = curr.next.next
                curr.next.data = curr.next.data.upper()
                curr = curr.next
                continue
            
            curr.data = " "
        curr = curr.next

    result = ""
    curr = list.head
    while curr != None:
        result += curr.data
        curr = curr.next
    return result

# print(string_beauty(string_ll))

# print(string_beauty(string_ll2))


duplicate_list = LinkedList()

for i in [10,10,20,20,30,30,30,40,40,50,50]:
    duplicate_list.append(i)

# print(duplicate_list)

def remove_duplicate(list):
    curr = list.head
    while curr != None:
        if curr.next != None:
            while curr.data == curr.next.data:
                if curr.next.next == None:
                    break
                curr.next = curr.next.next
        curr = curr.next

# remove_duplicate(duplicate_list)
# print(duplicate_list)
