p = 101
MOD = 1000000007

class Query:
	def __init__(self, L, R):
		self.L = L
		self.R = R

def is_palindrome(strng, L, R):

	while R > L:
		if strng[L] != strng[R]:
			return False
		L += 1
		R -= 1
	return True

def mod_pow(base, exponent):
	if exponent == 0:
		return 1
	if exponent == 1:
		return base

	temp = mod_pow(base, exponent // 2)

	if exponent % 2 == 0:
		return (temp % MOD * temp % MOD) % MOD
	else:
		return (((temp % MOD * temp % MOD) % MOD) * base % MOD) % MOD

def find_MMI(n):
	return mod_pow(n, MOD - 2)

def compute_prefix_hash(strng, n, prefix, power):
	prefix[0] = 0
	prefix[1] = ord(strng[0])

	for i in range(2, n + 1):
		prefix[i] = (prefix[i - 1] % MOD + (ord(strng[i - 1]) %
											MOD * power[i - 1] % MOD) % MOD) % MOD
	return

def compute_suffix_hash(strng, n, suffix, power):
	suffix[0] = 0
	suffix[1] = ord(strng[n - 1])

	for i in range(n - 2, -1, -1):
		j = n - i
		suffix[j] = (suffix[j - 1] % MOD + (ord(strng[i]) %
											MOD * power[j - 1] % MOD) % MOD) % MOD
	return


def query_results(strng, q, m, n, prefix, suffix, power):
	for i in range(m):
		L = q[i].L
		R = q[i].R

		hash_LR = ((prefix[R + 1] - prefix[L] + MOD) %
				MOD * find_MMI(power[L]) % MOD) % MOD

		reverse_hash_LR = ((suffix[n - L] - suffix[n - R - 1] + MOD) %
						MOD * find_MMI(power[n - R - 1]) % MOD) % MOD

		if hash_LR == reverse_hash_LR:
			if is_palindrome(strng, L, R) == True:
				print("The Substring [%d %d] is a palindrome" % (L, R))
			else:
				print("The Substring [%d %d] is not a palindrome" % (L, R))
		else:
			print("The Substring [%d %d] is not a palindrome" % (L, R))
	return

def compute_powers(power, n):

	power[0] = 1

	for i in range(1, n + 1):
		power[i] = (power[i - 1] % MOD * p % MOD) % MOD
	return


#Driver code
if __name__ == '__main__':
	strng = "abaaabaaaba"
	n = len(strng)

	power = [0] * (n + 1)
	compute_powers(power, n)

	prefix = [0] * (n + 1)
	suffix = [0] * (n + 1)

	compute_prefix_hash(strng, n, prefix, power)
	compute_suffix_hash(strng, n, suffix, power)

	q = [Query(0, 10), Query(5, 8), Query(2, 5), Query(5, 9)]
	m = len(q)

	query_results(strng, q, m, n, prefix, suffix, power)
