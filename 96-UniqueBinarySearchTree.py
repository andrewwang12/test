class Solution:
    def uniqueBST(self, n):
        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(1, n+1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[-1]

res = Solution()
n = 3
print(res.uniqueBST(n))