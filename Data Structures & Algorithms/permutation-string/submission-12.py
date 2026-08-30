class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if not s1 or not s2:
            return False
        
        count = Counter(s1)
        window = Counter(s2[:len(s1)])
        l = 0

        if window == count:
            return True
        
        for r in range(len(s1), len(s2)):
            window[s2[l]] -= 1
            l += 1
            window[s2[r]] += 1
            if window == count:
                return True
        return False