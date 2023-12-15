def coinChange(coins, amount):
    max_val = amount + 1
    dp = [max_val] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != max_val else -1

coins = [1, 2, 5]
amount = 11
result = coinChange(coins, amount)
print(result) 
