class Solution:
    def climbStairs(self, n:int) -> int:
        # edge case handling for 0 or 1 step
        if n<= 1:
            return 1

        dp = [0] * (n + 1)

        #Base case
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

        # n = 4
        # dp = [1,1,0,0]
        # for i = 2: dp[2] = dp[1] + dp[0] = 2
        # for i = 3: dp[3] = dp[2] + dp[1] = 3
        # for i = 4: dp[4] = dp[3] + dp[2] = 5

        # final result = 5 ways