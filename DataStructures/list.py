import ctypes
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