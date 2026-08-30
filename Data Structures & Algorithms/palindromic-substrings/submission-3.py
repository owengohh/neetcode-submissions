class Solution:
    def countSubstrings(self, s: str) -> int:
        count = [0]

        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                count[0] += 1
                i -= 1
                j += 1
        
        for i in range(len(s)):
            l = r = i
            expand(l, r)
            l, r = i, i+1
            expand(l, r)

        return count[0]