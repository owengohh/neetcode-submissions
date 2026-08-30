class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def bt(curr, i):
            if i >= len(s):
                res.append(curr[:])
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    curr.append(s[i:j+1])
                    bt(curr, j+1)
                    curr.pop()
        bt([], 0)
        return res
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True