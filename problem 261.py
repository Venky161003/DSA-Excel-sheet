from queue import PriorityQueue

def kthLargest(k, arr, n):
	ans = [0]*n

	pq = PriorityQueue()

	for i in range(n):

		if (pq.qsize() < k):
			pq.put(arr[i])
		else:
			if (arr[i] > pq.queue[0]):
				pq.get()
				pq.put(arr[i])

		if (pq.qsize() < k):
			ans[i] = -1
		else:
			ans[i] = pq.queue[0]

	return ans


#Driver Code
if __name__ == "__main__":
	n = 6
	arr = [1, 2, 3, 4, 5, 6]
	k = 4

	v = kthLargest(k, arr, n)
	print(*v)


