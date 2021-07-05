# Egg Drop With 2 Eggs and N Floors
class Solution:
    def twoEggDrop(self, n: int) -> int:
        k = 1
        while n-k > 0:
            n = n - k
            k = k + 1
        return k    
