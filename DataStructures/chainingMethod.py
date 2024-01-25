#-------- Implement hashing using chaining Method-----------------
class Node:
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0
    
    def append(self,key,data):
        new_node = Node(key,data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.n +=1
            return
        
        self.tail.next = new_node
        self.tail = new_node
        self.n += 1

    def __len__(self):
        return self.n
    
    def remove(self,key):    
        if self.head.key == key:
            self.head = self.head.next
            self.n -= 1
            return
        
        current_node = self.head
        
        while current_node.next != None:
            if current_node.next.key == key:
                break
            current_node = current_node.next
        
        if current_node.next == None:
            return "Item Not Found."
        else:
            current_node.next = current_node.next.next
            self.n -= 1
            return

    def traverse(self):
        current_node = self.head
        while current_node != None:
            print(f"{current_node.key}:{current_node.data}",end=",")
            current_node = current_node.next

    def search(self,key):        
        current_node = self.head
        pos = 0

        while current_node != None:
            if current_node.key == key:
                return pos
            current_node = current_node.next
            pos += 1

        return -1
    
    def get_node_at_index(self,index):
        pos = 0
        current_node = self.head
        while current_node != None:
            if pos == index:
                return current_node
            pos += 1
            current_node = current_node.next
    
class Dictionary:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        #Create an array of linked list
        self.buckets = self.make_array(self.capacity)

    def make_array(self,capacity):
        L = [] 
        for i in range(capacity):
            L.append(LinkedList())
        return L
    
    def hash_function(self,key):
        return abs(hash(key)) % self.capacity
    
    def __setitem__(self,key,value):
        self.put(key,value)

    def put(self,key,value):
        bucket_index = self.hash_function(key)
        node_index = self.get_node_index(bucket_index,key)

        if node_index == -1:
            #insertion
            self.buckets[bucket_index].append(key,value)
            self.size += 1
            load_factor = self.size / self.capacity
                        
            if load_factor >= 2:
                self.rehash()
        else:
            #updation
            self.buckets[bucket_index].get_node_at_index(node_index).data = value

    def __getitem__(self,key):
        return self.get(key)

    def get(self,key):
        bucket_index = self.hash_function(key)
        node_index = self.get_node_index(bucket_index,key)
        
        if node_index == -1:
            return "Not Found"
        else:
            return self.buckets[bucket_index].get_node_at_index(node_index).data
        
    
    def __delitem__(self,key):
        bucket_index = self.hash_function(key)
        node_index = self.get_node_index(bucket_index,key)

        if node_index == -1:
            return "Not Found"
        else:
            self.buckets[bucket_index].remove(key)
            self.size -= 1

    def get_node_index(self,bucket_index,key):
        node_index = self.buckets[bucket_index].search(key)
        return node_index
    
    def rehash(self):
        self.capacity = self.capacity * 2
        self.size = 0
        old_buckets = self.buckets
        self.buckets = self.make_array(self.capacity)

        for i in old_buckets:
            for j in range(len(i)):
                node = i.get_node_at_index(j)
                key,value = node.key,node.data
                self.put(key,value)

    def show(self):
        for i in range(self.capacity):
            print(i," = ",end="")
            self.buckets[i].traverse()
            print()




mydict = Dictionary(2)

mydict.put("Manish",26)
mydict.put("Vikas",29)
mydict.put("Avinash",31)
mydict.put("Sunita",54)
mydict.put("RSRai",59)

print("-----")
# print(mydict.size/mydict.capacity)
# del mydict["Manish"]
# print(mydict.size/mydict.capacity)
mydict.show()

