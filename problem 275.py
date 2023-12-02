d = 256

q = 103

def checkPalindromes(string):

	N = len(string)

	print string[0] + " Yes"

	if N == 1:
		return

	firstr = ord(string[0]) % q
	second = ord(string[1]) % q

	h = 1
	i = 0
	j = 0

	for i in xrange(1,N):

		if firstr == second:

			for j in xrange(0,i/2):
				if string[j] != string[i-j]:
					break
			j += 1
			if j == i/2:
				print string[i] + " Yes"
			else:
				print string[i] + " No"
		else:
			print string[i] + " No"

		if i != N-1:

			if i % 2 == 0:

				h = (h*d) % q
				firstr = (firstr + h*ord(string[i/2]))%q

				second = (second*d + ord(string[i+1]))%q
			else:

				second = (d*(second + q - ord(string[(i+1)/2])*h)%q
							+ ord(string[i+1]))%q

#Driver code
txt = "aabaacaabaa"
checkPalindromes(txt)




