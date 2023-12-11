MAX=256

MAX_WORD_LEN=500

class TrieNode:
	def __init__(self):
		self.child = [None] * MAX
		self.freq = 1

def newTrieNode():
	newNode = TrieNode()
	return newNode

def insert(root, str):
    
	len_str = len(str)
	pCrawl = root
	for level in range(len_str):

		index = ord(str[level])

		if not pCrawl.child[index]:
			pCrawl.child[index] = newTrieNode()
		else:
			pCrawl.child[index].freq += 1
		pCrawl = pCrawl.child[index]

def findPrefixesUtil(root, prefix, ind):

	if not root:
		return

	if root.freq == 1:
		prefix[ind] = ""
		print("".join(prefix[:ind]), end=" ")
		return
	for i in range(MAX):
		if root.child[i]:
			prefix[ind] = chr(i)
			findPrefixesUtil(root.child[i], prefix, ind + 1)

def findPrefixes(arr, n):
	root = newTrieNode()
	root.freq = 0
	
	for i in range(n):
		insert(root, arr[i])

	prefix = [None] * MAX_WORD_LEN

	findPrefixesUtil(root, prefix, 0)

# Driver code
if __name__ == "__main__":
	arr = ["zebra", "dog", "duck", "dove"]
	n = len(arr)
	findPrefixes(arr, n)
