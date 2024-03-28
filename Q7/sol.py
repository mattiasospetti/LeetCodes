# first approach: recursion
# consider it a a binary tree, dividi et impera --> 
# calculate the right and left subtriangle minimum path, then compare them (set the base case properly)
# it works, actually. But it's very time-demanding
 
class Solution(object):
    def minimumTotal(self, triangle):
       
        def solve(row,idx):
            if row == len(triangle)-1:
                return triangle[row][idx]
            return triangle[row][idx]+min(solve(row+1,idx),solve(row+1,idx+1))
        ans = solve(0,0)
        return ans
    
# alternative version, more spacially optimized
# store in the triangle the minimum path per each node, starting from leaves   

class Solution(object):
    def minimumTotal(self, triangle):
        len(triangle)
        for i in range(len(triangle)-2,-1,-1):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0] 