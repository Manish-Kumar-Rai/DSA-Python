#-----------------------Hashing ---------------------------------
class Dictionary:
    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size          #for storing keys
        self.data = [None] * self.size           #for storing data

    def put(self,key,value):
        hash_value = self.hash_function(key)
        
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] == value
            else:
                new_hash_value = self.rehash(hash_value)
                loop = 0
                while self.slots[new_hash_value] != None and self.slots[new_hash_value] != key and loop < self.size:
                    new_hash_value = self.rehash(new_hash_value)
                    loop += 1

                if self.slots[new_hash_value] == None:
                    self.slots[new_hash_value] = key
                    self.data[new_hash_value] = value
                elif self.slots[new_hash_value] == key:
                    self.data[new_hash_value] = value
                else:
                    print("no place left")

    def get(self,key):
        start_position = self.hash_function(key)
        current_position = start_position

        while self.slots[current_position] != None:
            if self.slots[current_position] == key:
                return self.data[current_position]
            
            current_position = self.rehash(current_position)

            if current_position == start_position:
                return "Not Found"
        
        return "Not Found"
    
    def __getitem__(self,key):
        return self.get(key)
                

    def __setitem__(self,key,value):
        self.put(key,value)

    def hash_function(self,key):
        """Return hahs_value for both slots and data list"""
        return abs(hash(key)) % self.size
    
    def rehash(self,old_hash):
        return (old_hash + 1) % self.size
    
    def __str__(self):
        result = "{"
        for i in range(len(self.slots)):
            if self.slots[i] != None:
                result += f"{self.slots[i]}:{self.data[i]}, "
        return result[:-2] + "}"    
        
    def __len__(self):
        pos = 0
        for i in range(len(self.slots)):
            if self.slots[i] != None:
                pos += 1
        return pos
    

# mydict = Dictionary(5)
# mydict.put("manish",26)
# mydict.put("vikas",29)
# mydict.put("avinash",32)
# mydict.put("sunita",55)
# mydict.put("rsrai",58)
# mydict.put("kiaan",1)
# print(mydict)
# print(len(mydict))
