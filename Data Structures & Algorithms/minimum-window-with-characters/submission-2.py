class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        min_len = float("inf")
        min_start = 0
        l = 0
        need = Counter(t)
        required = len(t)
        
        for r, ch in enumerate(s):
            if need[ch] > 0: # track number of chars we still need
                required -= 1
            need[ch] -= 1

            print(need)

            while required == 0:
                window_len = r - l + 1
                if window_len < min_len:
                    min_len = window_len
                    min_start = l
                
                left_ch = s[l]
                need[left_ch] += 1
                if need[left_ch] > 0:
                    required += 1
                l += 1

        return "" if min_len == float('inf') else s[min_start:min_start+min_len]