class Solution {
  
    long long int countBT(int h) {  
        long long int mod = 1000000007;   
        long long int dp[h + 1]; 
        // base cases 
        dp[0] = dp[1] = 1; 
        // iterating from 2 to h
        for(int i = 2; i <= h; i++) { 
            // calculating the number of binary trees for the current height
            dp[i] = (dp[i - 1] * ((2 * dp [i - 2])%mod + dp[i - 1])%mod) % mod; 
        } 
        return dp[h]; 
    }
}
