def removal(a, n, k):

a.sort()

diff = 0 
ans = 0

j = 0

for i in range(n):
	diff = a[i] - a[j]

	while(i >= j and diff > k):
	j += 1
	diff = a[i] - a[j]

	ans = max(ans, i-j+1)

	return n-ans

	a = [1, 3, 4, 9, 10, 11, 12, 17, 20]
	n = len(a)
	k = 4

	print(removal(a, n, k))
