from typing import List

class Solution:
    def uniqueRow(self, row : int, col : int, M : List[List[int]]) -> List[List[int]]:
        st = set() 
        vec = [] 
        
        for i in range(row):
            curr = ''
            for j in range(col):
                curr += str(M[i][j])  
            st.add(curr) 
            
        for i in range(row):
            curr = ''
            for j in range(col):
                curr += str(M[i][j]) 
            if curr in st: 
                st.remove(curr)  
                demo = []
                for j in range(col):
                    demo.append(M[i][j])  
                vec.append(demo)
                
        return vec 
