def sum(arr):
    total = 0
    for x in arr:
        total+= x
    return total

print (sum([2,3,4,6]))

def recursive_sum(arr):
    sum = 0
    if arr == 1:
        return arr[len(arr)-1]
    sum += arr[len(arr)-1] + recursive_sum(arr.pop())

print (recursive_sum([1,2,3]))
