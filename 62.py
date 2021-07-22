# Unique Paths
from math import factorial as fac
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(fac(m+n-2)/fac(m-1)/fac(n-1))