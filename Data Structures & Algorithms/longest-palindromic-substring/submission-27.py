class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_i = [0]
        res_length = [0]

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > res_length[0]:
                    res_length[0] = r-l+1
                    res_i[0] = l
                l -= 1
                r += 1

            

        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)

        return s[res_i[0]:res_i[0]+res_length[0]] 