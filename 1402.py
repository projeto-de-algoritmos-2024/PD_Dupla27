from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort()
        
        n = len(satisfaction)

        dp = [[-1] * (n + 1) for _ in range(n + 1)]

        def solve(i, j):
            if i == n:
                return 0 
            if dp[i][j] != -1:
                return dp[i][j]  
            
            option1 = solve(i + 1, j)
            
            option2 = satisfaction[i] * j + solve(i + 1, j + 1)

            dp[i][j] = max(option1, option2)
            return dp[i][j]
        return solve(0, 1)