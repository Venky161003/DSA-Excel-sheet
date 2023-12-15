def copySetBits(x, y, l, r):

	if (l < 1 or r > 32):
		return x;

	for i in range(l, r + 1):

		mask = 1 << (i - 1);

		if ((y & mask) != 0):
			x = x | mask;
	return x;

# Driver code
if __name__ == '__main__':
	x = 10;
	y = 13;
	l = 1;
	r = 32;
	x = copySetBits(x, y, l, r);
	print("Modified x is ", x);

