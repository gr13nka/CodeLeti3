import ctypes
import random
import time
import numpy
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

    def __len__(self):
        return self.size
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
    CopyCntL = 0
    CopyCntR = 0

    while i < len1 and j < len2:

        if left[i] <= right[j]:
            arr[k] = left[i]
            CopyCntL += 1
            CopyCntR = 0
            i += 1
        #galop
        elif CopyCntL > 7:
            rememberi = i
            galopcnt = 1

            while left[i] < right[j]:
                i += 2 ** galopcnt
                galopcnt += 1
            for z in range(i - rememberi):
                arr[z] = left[z]

        elif CopyCntR > 7:
            rememberj = j
            galopcnt = 1

            while right[j] < left [i]:
                j += 2**galopcnt
                galopcnt+=1
            for z in range(j-rememberj):
                arr[z] = right[z]

        else:
            arr[k] = right[j]
            CopyCntR += 1
            CopyCntL = 0
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
def timSort(arr):

    n = len(arr)
    minRun = calcMinRun(n)
    cntL = 0 #less
    cntM = 0 #more
    cnt = 0
    runs = []
#clever insertion
    for i in range(0, n-1):
        if arr[i+1] < arr[i]:
            cntL += 1

        elif arr[i+1] > arr[i]:
            cntM +=1

        elif cntL != 0:
            end = max(i + minRun-1, cntL)
            insertionSort(arr,i,end)
            runs.insert(cnt,i)
            runs.insert(cnt+1, end-i+1)
            cnt += 2
            cntL = 0

        elif cntM != 0:
            end = max(i + minRun-1, cntM)
            insertionSort(arr,i, end)
            runs.insert(cnt,i)
            runs.insert(cnt+1, end-i+1)
            cnt += 2
            cntM = 0

#merging

    # runs_stack = []
    #
    # for i in range(len(runs)/2):
    #     runs_stack[i] = runs[i]
    #     runs_stack[i+1] = runs[i+1]
    #     if (runs_stack[i+1] > runs_stack[i+1-2] + runs_stack[i+1-4]) and (runs_stack[i+1-2] > runs_stack[i+1-4]):
    #         merge(runs_stack[i+1],runs_stack[i+1-2])
    #     else:
    #         smaller = min(runs_stack[i+1],runs_stack[i+1-4])
    #         merge(runs_stack[i+1-2],smaller)

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


def getMinrun(arr,n):
    r = 0
    while n >= 64:
        r = r | (n & 1)
        n //= 2
    return n + r

def binaryInsertionSort(arr, n):
    if n <= 1:
        return arr

    for i in range(1, n):
        index = binarySearch(arr, 0, i - 1, arr[i])
        arr = arr[:index] + [arr[i]] + arr[index:i] + arr[i + 1:]

    return arr


def binarySearch(arr, l, r, key):

    if l == r:
        if arr[l] > key:
            return l
        else:
            return l + 1
    elif l > r:
        return l
    else:
        m = (l + r) // 2
        if arr[m] > key:
            return binarySearch(arr, l, m - 1, key)
        elif arr[m] < key:
            return binarySearch(arr, m + 1, r, key)
        else:
            return m


def reverse(arr,n):
    for i in range(0, n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]


def merge(left, right,n):
    l = 0
    r = 0
    res = []

    while l < len(left) and r < len(right):
            if l < len(left) and left[l] < right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1

    if r == len(right):
        res += left[l:]
    else:
        res += right[r:]

    return res

def mergeSort(arr,n):
    if n == 1:
        return arr

    left = mergeSort(arr[:n // 2],n)
    right = mergeSort(arr[n // 2:],n)
    return merge(left, right)

def timsort(arr,n):
    """ The man himself """

    minrun = getMinrun(arr,n)

    res = []

    stack = []
    runs = []
    run = []

    i = 0
    while i <= n:
        if len(run) < 2:
            run.append(arr[i])
            i += 1
            continue

        order = run[-1] - run[-2]

        # if current element ruins ordering - end current run
        if i >= n or (arr[i] >= run[-1] and order < 0) or (arr[i] < run[-1] and order >= 0):
            if len(run) < minrun:
                # if current run len is less than minrun -- fill current run till len == minrun
                if i + minrun < n:
                    run += arr[i:i + minrun]
                else:
                    run += arr[i:n]
                # hence gotta sort the shie
                run = binaryInsertionSort(run, n)
                i += minrun
            elif len(run) >= minrun and order < 0:
                # if all good but the ordering was reversed -- reverse current run
                reverse(run,n)

            runs.append(run.copy())
            run = []

            if i != n:
                i -= 1
        else:
            run.append(arr[i])

        i += 1

    while len(runs) > 0:
        if len(runs) == 1:
            res = runs.pop()
        elif len(runs) == 2:
            res = merge(runs.pop(), runs.pop(), n)
        else:
            x = runs.pop()
            y = runs.pop()
            z = runs.pop()

            if not (len(x) > len(y) + len(z)) or not (len(y) > len(z)):
                if len(x) >= len(z):
                    z = merge(z, y,n)
                else:
                    x = merge(x, y,n)

                runs.append(z)
                runs.append(x)
            else:
                runs.append(z)
                runs.append(y)
                runs.append(x)

    return res



if __name__ == "__main__":

    arr = DynamicArray()
    for i in range(100):
        arr.append(numpy.random.random_integers(10))
    print("Given Array is")
    print(arr)

    before = time.time()
    timSort(arr.array)
    after = time.time()

    # print("Sorting time", after-before)
    print(arr)
