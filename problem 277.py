def sumoflength(arr, n): 

	s = [] 

	j = 0
	ans = 0

	for i in range(n): 

		while (j < n and (arr[j] not in s)): 
			s.append(arr[j]) 
			j += 1

		ans += ((j - i) * (j - i + 1)) // 2

		s.remove(arr[i]) 

	return ans 

#Driven Code 
if __name__=="__main__": 
	
	arr = [1, 2, 3, 4] 
	n = len(arr) 
	print(sumoflength(arr, n)) 
