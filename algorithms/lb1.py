import ctypes
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None
class LinkedList:
    def __init__(self):
        self.head = Node()
        #self.tail = Node()
    def append (self, data):
        newNode = Node(data)
        currentNode = self.head

        while currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = newNode
    def length(self):
        cur = self.head
        cnt = 0
        while (cur.next):
            cur= cur.next
            cnt+=1
        return cnt
    def display(self):
        elems = []
        cur = self.head
        while (cur.next):
            cur = cur.next
            elems.append(cur.data)
        print (elems)

    def get(self, idx):
        if idx >= self.length() or idx < 0:
            print("too big")
            return None

        cur = self.head
        cnt = 0
        while cnt <= idx:
            cur = cur.next
            cnt += 1
        return cur.data
    def remove(self,idx):
        if idx >= self.length() or idx < 0:
            print("too big")
            return None

        cur = self.head
        cnt = 0
        while cnt <= idx:
            last = cur
            cur = cur.next
            cnt += 1
        last.next = cur.next
        return
class DynamicArray:
    def __init__(self, size=0, capacity=2):
        self.size = size
        self.capacity = capacity
        self.array = self.make_array(self.capacity)

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()
    def grow(self):
        self.capacity += 2

    def shrink(self):
        self.capacity -= 1

    def isEmpty(self):
        return self.size == 0

    def changeArray(self):
        list = self.make_array(self.capacity)
        for i in range(self.size):
            list[i] = self.array[i]
        self.array = list
    def append(self, data):
        if(self.size == self.capacity):
            self.grow()
            self.changeArray()

        self.array[self.size] = data
        self.size += 1

    def insert(self, idx, data):
        if (self.size == self.capacity):
            self.grow()
            self.changeArray()

        for i in range(self.size, idx, -1):
            self.array[i+1] = self.array[i]
        self.array[idx] = data
        self.size +=1

    def remove(self, idx):
        for i in range(idx, self.size-1):
            self.array[i] = self.array[i+1]
        self.array[self.size-1] = 0

        self.shrink()
        self.size -= 1
        self.changeArray()

    def search(self, idx):
        if idx >= 0 or idx < self.size:
            return self.array[idx]
        print("too big")

class Stack:
    def __init__(self):
        self.elem = []
    def is_empty(self):
        return len(self.elem) == 0
    def push(self,data):
        self.elem.append(data)
    def pop(self):
        if not self.is_empty():
            return self.elem.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.elem[-1]
        else:
            return None
def SortingStation(istream):
    expression = istream.split()
    operator_stack = Stack()
    ostream = ""

    operations = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3,
        "sin": 4,
        "cos": 4
    }

    for current in expression:
        if current.isdigit():
            ostream+=current
#        elif current == "sin" or current == "cos":
 #           operator_stack.push(current)
  #          while operator_stack.peek() != '(':
   #             ostream += operator_stack.pop()

        elif current in operations:
            while (not operator_stack.is_empty() and operator_stack.peek() != '(' and operations[operator_stack.peek()] >= operations[current]):
                ostream += operator_stack.pop()
            operator_stack.push(current)

        elif current == '(':
            operator_stack.push(current)

        elif current == ')':
            while ( not operator_stack.is_empty() and operator_stack.peek() != '('):
                ostream += operator_stack.pop()
            if operator_stack.peek() == '(':
                operator_stack.pop()
            elif operator_stack.peek() == "sin" or operator_stack.peek() == "cos":
                ostream += operator_stack.pop()



    while not operator_stack.is_empty():
        ostream += operator_stack.pop()
    return ostream


list = LinkedList()
list.append(1)
list.append(2)
list.append(2)
list.append(2)
list.display()
list.remove(0)
list.display()

dlist = DynamicArray()
dlist.insert(0,0)
dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.append(4)
for i in range(5):
    print(dlist.array[i])
print("-----------------")
dlist.remove(2)
for i in range(4):
    print(dlist.array[i])
print("-----------------")


print(SortingStation("sin ( 1 + 1 ) * 3 + cos ( 1 ) "))
