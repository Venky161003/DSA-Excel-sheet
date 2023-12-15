def square(n):

	if (n < 0):
		n = -n

	res = n

	for i in range(1, n):
		res += n

	return res


# Driver Code
for n in range(1, 6):
	print("n =", n, end=", ")
	print("n^2 =", square(n))
