# Count Sorted Vowel Strings
class Solution:
    def countVowelStrings(self, n: int) -> int:
      # before [a,b,c,d,e]
      # curr [a+b+c+d+e,b+c+d+e,c+d+e,d+e,e]
        curr = [1,1,1,1,1]
        if n == 1:
            return sum(curr)
        for _ in range(n-1):
            for j in range(3,-1,-1):
                curr[j]+=curr[j+1]
        return sum(curr)
            
