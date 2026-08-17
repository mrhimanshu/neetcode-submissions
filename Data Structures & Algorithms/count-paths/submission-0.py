class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n==1 or m==1:
            return 1
        else:
            return self.uniquePaths(n, m-1) + self.uniquePaths(n-1,m)
        