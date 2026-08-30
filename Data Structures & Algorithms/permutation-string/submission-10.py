class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if not s1 or not s2:
            return False

        count_s1 = Counter(s1)
        window = Counter(s2[:len(s1)])
        l = 0

        if window == count_s1:
            return True

        for r in range(len(s1), len(s2)):
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1
            window[s2[r]] += 1
            if window == count_s1:
                return True
        return False