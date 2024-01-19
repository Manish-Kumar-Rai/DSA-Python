# ---------------- Heap Class based on quasi-perfect binary tree------------------
# module for heap in python : - heapq which make an list heap

class OurHeap:
    def __init__(self,items):
        self.heap = [None]   # index 0 will be ignore
        self.rank = {}
        for x in items:
            self.push(x)

    def __len__(self):
        return len(self.heap) - 1
    
    def push(self,x):
        assert x not in self.rank
        i = len(self.heap)
        self.heap[i] = x
        self.rank[x] = i 
        self.up(i)                          #Maintain Heap Order

    def pop(self):
        root = self.heap[1]
        del self.rank[root]
        x = self.heap.pop()                 # remove the last leaf
        if self:                            # if heap is not empty
            self.heap[1] = x
            self.rank[x] = 1
            self.down(1)
        return root
    
    def up(self,i):
        x = self.heap[i]
        while (i > 1 and x < self.heap[i//2]):
            self.heap[i] = self.heap[i//2]
            self.rank[self.heap[i//2]] = i
            i //= 2
        self.heap[i] = x                   #insertion index found
        self.rank[x] = i

    def down(self,i):
        x = self.heap[i]
        n = len(self.heap)
        while True:
            left = 2 * i
            right = left + 1
            if (i < n and self.heap[right] < x and self.heap[right] < self.heap[left]):
                self.heap[i] = self.heap[right]
                self.rank[self.heap[right]] = i  #move right child up
                i = right
            elif (i < n and self.heap[left] < x):
                self.heap[i] = self.heap[left]
                self.rank[self.heap[left]] = i    # move left child up
                i = left
            else:
                self.heap[i] = x                   # insertion index found
                self.rank[x] = i
                return
    
    def update(self,old,new):
        i = self.rank[old]
        del self.rank[old]
        self.heap[i] = new
        self.rank[new] = i
        if old < new:
            self.down(i)
        else:
            self.up(i)