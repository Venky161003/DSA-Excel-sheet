class Solution{

    int maxSquare(int n, int m, vector<vector<int>> mat){

        int sub[n][m], maxsize = 0;

        for(int i = 0;i < m;i++){
            sub[0][i] = mat[0][i];
            maxsize = max(maxsize, sub[0][i]);
        }

        for(int i = 0;i < n;i++){
            sub[i][0] = mat[i][0];
            maxsize = max(maxsize, sub[i][0]);
        }

        for(int i = 1;i < n;i++){
            for(int j = 1;j < m;j++){
                if(mat[i][j] == 1)
                    sub[i][j] = min(sub[i-1][j-1], 
                                min(sub[i][j-1], sub[i-1][j])) + 1;
                else
                    sub[i][j]=0;
                maxsize = max(maxsize, sub[i][j]);
            }
        }

        return maxsize;
    }
}
