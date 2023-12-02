import sys
 
def kthSmallest(arr, l, r, K):
 
    if (K > 0 and K <= r - l + 1):
 
        pos = partition(arr, l, r)
 
        if (pos - l == K - 1):
            return arr[pos]
        if (pos - l > K - 1):  
            return kthSmallest(arr, l, pos - 1, K)
 
        return kthSmallest(arr, pos + 1, r,
                           K - pos + l - 1)
 
    return sys.maxsize
 

def partition(arr, l, r):
 
    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i
 


 
if __name__ == "__main__":
 
    arr = [12, 3, 5, 7, 4, 19, 26]
    N = len(arr)
    K = 3
    print("K'th smallest element is",
          kthSmallest(arr, 0, N - 1, K))
 


