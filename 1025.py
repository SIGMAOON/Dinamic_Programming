# Divisor Game
class Solution:
    def divisorGame(self, n: int) -> bool:
        count = 0
        while n!=1:
            for x in range(1,n):
                if n%x == 0:
                    break
            n = n - x
            count+=1
        if count%2 == 0:
            return False
        return True
        
      