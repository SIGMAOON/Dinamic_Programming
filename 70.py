# Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        answer = [1,2,3]
        if n <= 3:
            return answer[n-1]
        else:
            for i in range(3,n):
                answer.append(answer[-1] + answer[-2])
        return answer[n-1]