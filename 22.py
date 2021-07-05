# Generate Parentheses
class Solution:
    def generateParenthesis(self, n):
        dp = {1: set(['()']), 2: set(['(())', '()()'])}
        if n < 3:
            return list(dp[n])
        
        for i in range(3, n+1):
            dp[i] = set(['(' + x + ')' for x in dp[i-1]])
            for j in range(1, i):
                # 합집합으로 중복제거
                dp[i] = dp[i].union([x + y for x in dp[j] for y in dp[i-j]])
                
        return list(dp[n])