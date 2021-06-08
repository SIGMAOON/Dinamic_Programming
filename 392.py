# Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = []
        def findindex(find,string):
            for i in range(len(string)):
                if string[i] == find:
                    return i
            return -1
        for letter in s:
            a = findindex(letter,t)
            if a == -1:
                return False
            else:
                idx.append(a)
                t = t[a+1:]
        if len(idx) == len(s):
            return True
        return False
