import ctypes
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None
class LinkedList:

    MIN_MERGE = 32
    def __init__(self):
        self.head = Node()
        self.tail = Node()
    def append (self, data):
        newNode = Node(data)
        currentNode = self.head
        tmpNode = Node(data)

        while currentNode.next != None:
            tmpNode = currentNode
            currentNode.previous = tmpNode
            currentNode = currentNode.next

        currentNode.previous = tmpNode
        currentNode.next = newNode

        if self.length() == 1:
            self.tail = newNode

    def length(self):
        cur = self.head
        cnt = 0
        while (cur.next):
            cur = cur.next
            cnt += 1
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
    def insert(self,data,idx):
        self.append(0)
        cur = self.head

        for i in range(self.length(), idx, -1):
            print("curent ", cur.data)
            print("previous ", cur.previous.data)
            cur.data = cur.previous.data
            cur = cur.previous

        self.display()
        print(i)

        cur.data = data

    def replace(self,data,idx):
        if idx >= self.length() or idx < 0:
            print("too big")
            return None
        self.insert(data,idx)
        self.remove(idx)
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
    MIN_MERGE = 32
    def __init__(self):
        self.size = 0
        self.capacity = 2
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



MIN_MERGE = 32


def calcMinRun(n):
    """Returns the minimum length of a
    run from 23 - 64 so that
    the len(array)/minrun is less than or
    equal to a power of 2.

    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
    ..., 127=>64, 128=>32, ...
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
def merge(arr, l, m, r):

    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # Copy remaining elements of left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    # Copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


# Iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def timSort(arr,n):
    minRun = calcMinRun(n)

    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)

    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = minRun
    while size < n:

        # Pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):

            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size


# Driver program to test above function
if __name__ == "__main__":

    arr = DynamicArray()
    a = [-2, 7, 15, -14, 0, 15, 0, 7, -7, -4, -13, 5, 8, -14, 12]
    for i in range(len(a)):
        arr.append(a[i])
    print("Given Array is")
    print(arr.array)
    #
    # # Function Call
    timSort(arr.array,arr.size)
    #
    print("After Sorting Array is")
    print(arr.array)
