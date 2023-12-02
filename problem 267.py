ALPHA = 26

def getDiffString(str):
   
    shift=""
 
    for i in range(1, len(str)):
        dif = (ord(str[i]) -
              ord(str[i - 1]))
 
        if(dif < 0):
            dif += ALPHA
 
        shift += chr(dif + ord('a'))
 
    return shift
 
def groupShiftedString(str,n):
 
    groupMap = {}
 
    for i in range(n):
        diffStr = getDiffString(str[i])
        if diffStr not in groupMap:
            groupMap[diffStr] = [i]
        else:
            groupMap[diffStr].append(i)
     
    for it in groupMap:
        v = groupMap[it]
        for i in range(len(v)):
            print(str[v[i]], end = " ")
        print()
         
#Driver code
str = ["acd", "dfg", "wyz", 
       "yab", "mop","bdfh", 
       "a", "x", "moqs"]
n = len(str)
groupShiftedString(str, n)
 
