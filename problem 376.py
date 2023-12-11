def countDer(n):

	der = [0 for i in range(n + 1)]

	der[1] = 0
	der[2] = 1

	for i in range(3, n + 1):
		der[i] = (i - 1) * (der[i - 1] +
							der[i - 2])

	return der[n]

# Driver Code
n = 4
print("Count of Derangements is ", countDer(n))

