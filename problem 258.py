def maxRepeating(arr, n,  k):
 
    for i in range(0,  n):
        arr[arr[i]%k] += k
 
    max = arr[0]
    result = 0
    for i in range(1, n):
     
        if arr[i] > max:
            max = arr[i]
            result = i
 
    return result
 
 
arr = [2, 3, 3, 5, 3, 4, 1, 7]
n = len(arr)
k = 8
print("The maximum repeating number is",maxRepeating(arr, n, k))
