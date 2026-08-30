class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_len = [0]
        res_i = [0]

        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > res_len[0]:
                    res_i[0] = l
                    res_len[0] = r-l+1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            helper(i, i)
            helper(i, i+1)

        return s[res_i[0]:res_i[0]+res_len[0]]
