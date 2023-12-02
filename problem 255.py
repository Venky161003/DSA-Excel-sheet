def partition(arr, l, r):
	x = arr[r] 
	i = l

	for j in range(l, r):
		if arr[j] <= x:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1

	arr[i], arr[r] = arr[r], arr[i]
	return i

def kthLargest(arr, l, r, k, N):

	pos = partition(arr, l, r)

	if pos - l == k - 1:
		return
	    
	elif pos - l < k - 1:
		kthLargest(arr, pos + 1, r, k - pos + l - 1, N)

	else:
		kthLargest(arr, l, pos - 1, k, N)

if __name__ == "__main__":
	arr = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
	N = len(arr)
	k = 3
	
	kthLargest(arr, 0, N - 1, k, N)

	print(f"{k} largest elements are:", end=" ")
	for i in range(N - 1, N - k - 1, -1):
		print(arr[i], end=" ")

	print()
