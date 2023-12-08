def permutationCoeff(n, k):

f=1
	
for i in range(k): 
	f*=(n-i)
		
return f

# Driver Code
n = 10
k = 2
print("Value of P(", n, ", ", k, ") is ",
		permutationCoeff(n, k))
