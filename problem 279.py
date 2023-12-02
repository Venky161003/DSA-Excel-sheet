import heapq

def KMaxCombinations(a, b, k):
	
	a.sort()
	b.sort()
	
	n = len(a)
	
	pq = []
	heapq.heapify(pq)
	pq.append((-a[n-1] - b[n-1], (n - 1, n - 1)))
	
	my_set = set() 
	my_set.add((n - 1, n - 1))
	
	
	
	for count in range(K):
		
		temp = heapq.heappop(pq)
		
		print(-temp[0])
		
		i = temp[1][0]
		j = temp[1][1]
		sum = a[i - 1] + b[j]
		
		temp1 = (i - 1, j)
		

		if(temp1 not in my_set):
			heapq.heappush(pq, (-sum, temp1))
			my_set.add(temp1)
		
		sum = a[i] + b[j - 1]
		
		temp1 = (i, j - 1)
		

		if(temp1 not in my_set):
			heapq.heappush(pq, (-sum, temp1))
			my_set.add(temp1)



#Driver Code.
A = [ 1, 4, 2, 3 ];
B = [ 2, 5, 1, 6 ];
K = 4;

KMaxCombinations(A, B, K);

