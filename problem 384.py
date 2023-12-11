from typing import List, Tuple
from collections import defaultdict

def sum_zero(temp: List[int], starti: List[int], endj: List[int], n: int) -> bool:
	presum = defaultdict(int)
	sum_ = 0
	# Initialize length of sub-array with sum 0
	max_length = 0
	for i in range(n):
		sum_ += temp[i]
		if temp[i] == 0 and max_length == 0:
			starti[0] = i
			endj[0] = i
			max_length = 1
		if sum_ == 0:
			if max_length < i + 1:
				starti[0] = 0
				endj[0] = i
			max_length = i + 1
		if sum_ in presum:
			old = max_length
			max_length = max(max_length, i - presum[sum_])
			if old < max_length:
				endj[0] = i
				starti[0] = presum[sum_] + 1
		else:
			presum[sum_] = i
	return max_length != 0

def sum_zero_matrix(a: List[List[int]], row: int, col: int) -> None:
	temp = [0] * row
	fup = fdown = fleft = fright = 0
	maxl = float('-inf')

	for left in range(col):
		temp = [0] * row

		for right in range(left, col):

			for i in range(row):
				temp[i] += a[i][right]
			up, down = [0], [0]

			s = sum_zero(temp, up, down, row)
			ele = (down[0] - up[0] + 1) * (right - left + 1)

			if s and ele > maxl:
				fup = up[0]
				fdown = down[0]
				fleft = left
				fright = right
				maxl = ele

	if fup == fdown == fleft == fright == 0 and a[0][0] != 0:

		print("No zero-sum sub-matrix exists")
		return
	for j in range(fup, fdown+1):
		for i in range(fleft, fright+1):
			print(a[j][i], end=" ")
		print()


# Driver code
if __name__ == '__main__':
	a = [[9, 7, 16, 5],
		[1, -6, -7, 3],
		[1, 8, 7, 9],
		[7, -2, 0, 10]]
	row, col = 4, 4
	sum_zero_matrix(a, row, col)

