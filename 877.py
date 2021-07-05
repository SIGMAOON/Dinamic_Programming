# Stone Game
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        Alex = 0
        Lee = 0
        
        piles.sort()
        
        l = len(piles)
        
        for i in range(l):
            if i%2 == 0:
                Alex+=piles.pop()
            else:
                Lee+=piles.pop()
                
        if Alex > Lee:
            return True
        else:
            return False
        
