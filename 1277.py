# Count Square Submatrices with All Ones
from copy import deepcopy
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def dinamic(lis):
            dp = deepcopy(lis)
            
            m = len(lis)
            n = len(lis[0])

            for i in range(1,m):
                for j in range(1,n):
                    if matrix[i][j] == matrix[i-1][j] == matrix[i][j-1] == matrix[i-1][j-1] and matrix[i][j] != 0:
                        dp[i][j]+=1
            return dp
        
        while True:
            if matrix == dinamic(matrix):
                break
            else:
                matrix = dinamic(matrix)
        
        return sum([sum(a) for a in matrix])
