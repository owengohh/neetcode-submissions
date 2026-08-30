class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        l = 0 
        longest = 0

        for r in range(len(s)):
            counter[s[r]] += 1
            while max(counter.values()) + k < (r-l+1):
                counter[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
        return longest
