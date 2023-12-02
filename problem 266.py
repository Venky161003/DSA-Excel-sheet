from collections import defaultdict


def countDistinct(arr, K, N):

	mp = defaultdict(lambda: 0)

	dist_count = 0

	for i in range(K):
		if mp[arr[i]] == 0:
			dist_count += 1
		mp[arr[i]] += 1

	print(dist_count)

	for i in range(K, N):

		if mp[arr[i - K]] == 1:
			dist_count -= 1
		mp[arr[i - K]] -= 1

		if mp[arr[i]] == 0:
			dist_count += 1
		mp[arr[i]] += 1

		print(dist_count)

# Driver's code
if __name__=='__main__':
arr = [1, 2, 1, 3, 4, 2, 3]
N = len(arr)
K = 4

countDistinct(arr, K, N)

