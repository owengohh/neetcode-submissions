class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        
        min_i = 0
        min_length = float('inf')
        l = 0
        need = Counter(t)
        required = len(t)

        for r, ch in enumerate(s):
            if need[ch] > 0:
                required -= 1
            need[ch] -= 1

            while required == 0:
                if (r-l+1) < min_length:
                    min_length = r-l+1
                    min_i = l

                left_ch = s[l]
                need[left_ch] += 1
                if need[left_ch] > 0:
                    required += 1
                l += 1
        
        return "" if min_length == float('inf') else s[min_i:min_i+min_length]