from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix_sums = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]

        dp = [[-1 for _ in range(n + 1)] for _ in range(n)]

        def solve(i, M):

            if i >= n:
                return 0

            if dp[i][M] != -1:
                return dp[i][M]

            max_stones = 0

            for x in range(1, 2 * M + 1):

                if i + x > n:
                    break

                current_stones = suffix_sums[i] - suffix_sums[i + x]

                next_M = max(M, x)

                remaining_stones = solve(i + x, next_M)

                max_stones = max(
                    max_stones, current_stones + (suffix_sums[i + x] - remaining_stones)
                )

            dp[i][M] = max_stones
            return dp[i][M]

        return solve(0, 1)
