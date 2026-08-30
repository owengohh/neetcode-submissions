class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def bt(i, curr):
            if i >= len(s):
                res.append(curr[:])
                return
            for j in range(i, len(s)):
                if self.isPali(i, j, s):
                    curr.append(s[i:j+1])
                    bt(j+1, curr)
                    curr.pop()
        
        bt(0, [])
        return res

    def isPali(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
