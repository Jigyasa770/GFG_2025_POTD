class Solution:
    def lcs(self, s1, s2):
        n = len(s1)
        m = len(s2)
        
        # Create a 2D array to store lengths of longest common subsequence.
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Build the dp array from bottom-up
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[n][m]
