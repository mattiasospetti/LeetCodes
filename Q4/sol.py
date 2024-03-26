# gotta be honest: this was kinda hard. The first attempt worked, but I used brute force (mainly due to the time left), so the complexity was incredibly high.
# After hours of deep thinking, I found this YT Video from Fraz, https://www.youtube.com/watch?v=8HYXkNB39KA, which proved to be useful.
# Here the idea is to iterate the matrix, elem by elem, considering each 1 as the top-left-most elem in a submatrix.
# the consequent dimension of this submatrix depends on the minimum common number of ones per each row

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
       
        m, n = len(mat), len(mat[0])
        count = 0
        
        # first of all, we start by calculating a mirror matrix, dp,
        # which counts the consecutive ones per each row

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    dp[i][j] = 1 if j == 0 else dp[i][j-1] + 1

        for i in range(m):
            for j in range(n):
                minWidth = float('inf')
                for k in range(i, -1, -1):
                    minWidth = min(minWidth, dp[k][j])
                    if minWidth == 0:
                        break
                    count += minWidth
        return count
