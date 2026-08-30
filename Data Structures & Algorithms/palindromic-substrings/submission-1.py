class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_pal(s):
            l,r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        substrings =  [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
        memo = set()
        count = 0
        for substring in substrings:
            if substring in memo:
                count += 1
                continue
            
            if is_pal(substring):
                memo.add(substring)
                count += 1
        return count