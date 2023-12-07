def merge(arr, l, m, r, hm):

	n1 = m - l + 1
	n2 = r - m

	L= [0 for i in range(n1)]
	R = [0 for i in range(n2)]

	for i in range(n1):
		L[i] = arr[l + i]

	for j in range(n2):
		R[j] = arr[m + 1 + j]

	i,j,k,c = 0,0,l,0
	while (i < n1 and j < n2):
		if (L[i] <= R[j]):

			if(L[i] in hm):
				hm[L[i]] += c
			else :
				hm[L[i]] = c
			arr[k] = L[i]
			k += 1
			i += 1
		else:
			arr[k] = R[j]

			c += 1
			k += 1
			j += 1

	while (i < n1):
		if(L[i] in hm):
			hm[L[i]] += c
		else :
			hm[L[i]] = c
		arr[k] = L[i]
		k += 1
		i += 1

	while (j < n2):
		arr[k] = R[j]
		k += 1
		j += 1


def mergeSort(arr,l,r,hm):
	if (l < r):
		m = l + (r - l) // 2
		mergeSort(arr, l, m, hm)
		mergeSort(arr, m + 1, r, hm)
		merge(arr, l, m, r, hm)

def printArray(arr,n):

	for i in range(n):
		print(arr[i],end = " ")
	print("")

def findSurpasser(arr, n):

	hm = {}

	dup = arr[:]

	mergeSort(dup, 0, n - 1, hm)

	print("Surpasser Count of array is ")
	for i in range(n):
		print((n - 1) - i - (hm[arr[i]] if arr[i] in hm else 0),end = " ")

#Driver program to test above functions 

arr = [ 2, 7, 5, 3, 0, 8, 1 ]
n = len(arr)

print("Given array is ")
printArray(arr, n)

findSurpasser(arr, n)

