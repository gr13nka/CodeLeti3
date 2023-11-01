import os
import random
import ctypes

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
def getMinrun(arr):
    n = len(arr)
    r = 0
    while n >= 64:
        r = r | (n & 1)
        n //= 2
    return n + r

def binaryInsertionSort(arr):
    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
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


def reverse(arr: list):
    for i in range(0, len(arr) // 2):
        arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]


def merge(left: list, right: list) -> list:
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

def timsort(arr: list) -> list:
    minrun = getMinrun(arr)
    res = []
    runs = []
    #current run
    run = []

    i = 0
    while i <= len(arr):

        if len(run) < 2:
            run.append(arr[i])
            i += 1
            continue

        order = run[-1] - run[-2]
        if i >= len(arr) or (arr[i] >= run[-1] and order < 0) or (arr[i] < run[-1] and order >= 0):
            if len(run) < minrun:
                if i + minrun < len(arr):
                    run += arr[i:i + minrun]
                else:
                    run += arr[i:len(arr)]
                run = binaryInsertionSort(run)
                i += minrun
            elif len(run) >= minrun and order < 0:
                reverse(run)

            runs.append(run.copy())
            run = []

            if i != len(arr):
                i -= 1
        else:
            run.append(arr[i])

        i += 1

    while len(runs) > 0:
        if len(runs) == 1:
            res = runs.pop()
        elif len(runs) == 2:
            res = merge(runs.pop(), runs.pop())
        else:
            x = runs.pop()
            y = runs.pop()
            z = runs.pop()

            if not (len(x) > len(y) + len(z)) or not (len(y) > len(z)):
                if len(x) >= len(z):
                    z = merge(z, y)
                else:
                    x = merge(x, y)

                runs.append(z)
                runs.append(x)
            else:
                runs.append(z)
                runs.append(y)
                runs.append(x)

    return res

a = DynamicArray()
for i in range(100):
    a.append(random.randint(0, 100))
print(timsort(a.array))
