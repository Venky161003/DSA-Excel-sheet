MAXN = 11

ver = 2

hashtable = [[float('inf')] * MAXN for _ in range(ver)]

pos = [0] * ver

def init_table():

	for i in range(ver):
		for j in range(MAXN):
			hashtable[i][j] = float('inf')

def hash(function, key):

	if function == 1:
		return key % MAXN
	elif function == 2:
		return (key // MAXN) % MAXN

def place(key, table_id, cnt, n):

	if cnt == n:
		print(f"{key} unpositioned")
		print("Cycle present. REHASH.")
		return

	for i in range(ver):
		pos[i] = hash(i + 1, key)
		if hashtable[i][pos[i]] == key:
			return

	if hashtable[table_id][pos[table_id]] != float('inf'):
		dis = hashtable[table_id][pos[table_id]]
		hashtable[table_id][pos[table_id]] = key
		place(dis, (table_id + 1) % ver, cnt + 1, n)
	else: 
		hashtable[table_id][pos[table_id]] = key

def print_table():
    
	print("Final hash tables:")
	for i in range(ver):
		print()
		for j in range(MAXN):
			if hashtable[i][j] == float('inf'):
				print("- ", end="")
			else:
				print(f"{hashtable[i][j]} ", end="")
	print()

def cuckoo(keys, n):

	init_table()

	for i in range(n):
		cnt = 0
		place(keys[i], 0, cnt, n)

	print_table()

#driver function
def main():
	
	keys_1 = [20, 50, 53, 75, 100, 67, 105, 3, 36, 39]

	cuckoo(keys_1, len(keys_1))

	keys_2 = [20, 50, 53, 75, 100, 67, 105, 3, 36, 39, 6]

	cuckoo(keys_2, len(keys_2))

if __name__ == "__main__":
	main()

