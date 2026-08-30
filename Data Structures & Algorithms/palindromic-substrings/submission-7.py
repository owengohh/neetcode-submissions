class Solution:
    def countSubstrings(self, s: str) -> int:
        count = [0]

        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count[0] += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            helper(i, i)
            helper(i, i+1)
        
        return count[0]