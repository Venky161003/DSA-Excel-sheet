def wordBreak(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  

    for i in range(1, n + 1):
        for word in wordDict:
            if i >= len(word) and s[i - len(word):i] == word:
                dp[i] = dp[i] or dp[i - len(word)]

    return dp[n]

s = "leetcode"
wordDict = ["leet", "code"]
result = wordBreak(s, wordDict)
print(result)  
