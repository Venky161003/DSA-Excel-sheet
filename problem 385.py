def solve(m,R,C):
	for i in range(R):
		for j in range(C):
			if m[i][j] == 0:
				m[i][j] = -1
				
	maxval =0
	temparr = [[0]*(C+1) for _ in range(R)]
	for i in range(C):
		for j in range(i, C):
			temp = []
			for k in range(R):
				
				if i==0:
					temparr[k][j+1] = temparr[k][j]+m[k][j]
					temp.append(temparr[k][j+1])
				else:
					temp.append(temparr[k][j+1]-m[k][i])
			
			maxval = max(maxval, getmax(temp)*(j-i+1))
			
	
	return maxval

def getmax(arr):
	
	dic = dict()
	currsum = 0
	maxlen = 0
	for i in range(len(arr)):
		currsum+= arr[i]
		
		if currsum ==0:
			maxlen = i+1
			
		
		if currsum not in dic:
			dic[currsum] = i
			
		else:
			temp = i- dic[currsum]
			
			maxlen = max(temp, maxlen)
			
	
	return maxlen



if __name__ == '__main__':

	m = [[0, 0, 1, 1],
					[0, 1, 1, 1]] 
	
	R = len(m)
	C = len(m[0])
	
	ans = solve(m, R, C)
	print(ans)
