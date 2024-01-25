
#-------------------- Stacks------------------
        
#Using linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.n = 0

    def push(self,item):
        node = Node(item)
        if self.isempty():
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.n += 1

    def pop(self):
        if self.isempty():
            return "Stack is Empty."
        
        item = self.top.data
        self.top = self.top.next
        self.n -= 1
        return item
    
    def peek(self):
        return self.top.data

    def isempty(self):
        return self.top == None

    def __len__(self):
        return self.n
    
    def __str__(self):
        curr = self.top
        result = ""
        while curr != None:
            result = result + str(curr.data) + "->"
            curr = curr.next
        return result[:-2]
    
# myStack = Stack()
# myStack.push("Rai")
# myStack.push("Kumar")
# myStack.push("Manish")
# print(myStack.isempty())
# print(myStack)

# print(myStack.pop())
# print(len(myStack))
# print(myStack.peek())
    

#Stack using list in python
    
class Stack2:
    def __init__(self,size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1

    def push(self,value):
        if self.top == self.size - 1:
            return "overflow"
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.top == -1 :
            return "Stack is empty"
        else:
            item = self.stack[self.top]
            self.top -= 1
            return item

    def traverse(self):
        for i in range(self.top+1):
            print(self.stack[i],end=" ")
# mystack = Stack2(3)
# mystack.push(4)
# mystack.push(5)
# mystack.push(6)
# print(mystack.pop())
# print(mystack.pop())
# print(mystack.pop())
# mystack.traverse()
# print(mystack.stack)
    
#--------------Question----------------
def reverse_string(text):
    stack = Stack()

    for i in str(text):
        stack.push(i)

    rev_string = ""
    while not stack.isempty():
        rev_string += stack.pop()
    
    return rev_string

# print(reverse_string("123456789"))

class UndoRedo:
    def __init__(self,text):
        self.main = Stack()
        self.backup = Stack()
        for i in text:
            self.main.push(i)

    def __str__(self):
        return str(self.main).replace("->","")[::-1]
    
    def undo(self):
        if self.main.isempty():
            return
        self.backup.push(self.main.pop())

    def redo(self):
        if self.backup.isempty():
            return
        self.main.push(self.backup.pop())
    
# myString = UndoRedo("Manish")
# print(myString)
# myString.undo()
# myString.undo()
# myString.undo()
# myString.undo()
# print(myString)
# myString.redo()
# myString.redo()
# myString.redo()
# myString.redo()
# print(myString)
        

def balanced_parenthesis(text):
    mystack = Stack()
    for i in text:
        if i == "{" or i == "(" or i == "[":
            mystack.push(i)
        if i == "}":
            if mystack.peek() == "{":
                mystack.pop()
        if i == ")":
            if mystack.peek() == "(":
                mystack.pop()
        if i == "]":
            if mystack.peek() == "[":
                mystack.pop()
    print(mystack.isempty())
    return mystack.isempty()

# balanced_parenthesis("[{(a+b)+(c+d)}]")

#Celebrity Problem---------------

matrix = [
    [0,0,1,1],
    [0,0,1,1],
    [1,0,0,1],
    [0,0,0,0]
]

def find_the_celeb(matrix):
    mystack = Stack()

    for i in range(len(matrix)):
        mystack.push(i)

    while len(mystack) >= 2:
        i = mystack.pop()
        j = mystack.pop()

        if matrix[i][j] == 0:
            # j is not a celebrity
            mystack.push(i)
        else:
            # i is not a celebrity
            mystack.push(j)

    celeb = mystack.pop()

    for i in range(len(matrix)):
        if i != celeb:
            if matrix[celeb][i] == 1 or matrix[i][celeb] == 0:
                return "No one is celebrity."
        
    return f"The celebrity is {celeb}."


# print(find_the_celeb(matrix))
