import heapq

def findClosestElements(arr, k, x):

	max_heap = []

	for num in arr:

		if num == x:
			continue

		diff = abs(num - x)
		heapq.heappush(max_heap, (-diff, num))

		if len(max_heap) > k:
			heapq.heappop(max_heap)

	result = []

	while max_heap:

		diff, num = heapq.heappop(max_heap)

		result.append(num)

	return sorted(result)


#Driver code
arr = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
k = 4
x = 35
res = findClosestElements(arr, k, x)
print(res)









