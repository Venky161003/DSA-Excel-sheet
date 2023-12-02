def find_kth_smallest_number(arr, k):
    max_num = max(arr)
     
    count = [0] * (max_num + 1)  
    for num in arr:
        count[num] += 1
         
    num = 1
    
    while k > 0:
        if num < len(count) and count[num] > 0:
            count[num] -= 1
        else:
            k -= 1
        num += 1
         
    return num - 1  
 
def main():
    arr = [1, 3]
    k = 4
     
    kth_smallest = find_kth_smallest_number(arr, k)
    print("K-th smallest number:", kth_smallest)
 
if __name__ == "__main__":
    main()


















