class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = defaultdict(int)
        l = 0
        longest = 0
        for r in range(len(s)):
            charMap[s[r]] += 1
            while max(charMap.values()) + k < (r - l + 1):
                charMap[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
        return longest
