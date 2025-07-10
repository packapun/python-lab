def count_rec(coins, n, sum):
    if sum == 0:
        return 1
    if sum < 0 or n == 0:
        return 0    
    return  count_rec(coins, n, sum - coins[n-1]) + count_rec(coins,n-1,sum)

def count(coins,sum):
    n = len(coins)
    dp = [0] * (sum+1)
    dp[0] = 1

    for i in range(n):
        for j in range(coins[i], sum+1):
            dp[j] += dp[j - coins[i]]
            print(dp)
    return dp[sum]
coins = [1,2,3]
sum = 5
print(count(coins,sum))