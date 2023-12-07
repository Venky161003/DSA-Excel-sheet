class Solution:

    def shortest_distance(self, matrix):
        
        INF = 1<<32 
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = INF

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] < INF and matrix[k][j] < INF and matrix[i][k] + matrix[k][j] < INF:
                        matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        for i in range(n):
            for j in range(n):
                if matrix[i][j] >= INF:
                    matrix[i][j] = -1
