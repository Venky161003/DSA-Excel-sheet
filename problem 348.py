def numDecodings(s):
    n = len(s)

    if n == 0 or s[0] == '0':
        return 0

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):

        if 1 <= int(s[i - 1]) <= 9:
            dp[i] += dp[i - 1]

        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[n]

s = "11106"
result = numDecodings(s)
print(result)  
