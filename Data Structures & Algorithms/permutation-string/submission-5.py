class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        if len(s1) > len(s2):
            return False
        
        counter_s1 = Counter(s1)
        counter_window = Counter(s2[:len(s1)])

        if counter_window == counter_s1:
            return True
        
        
        for i in range(len(s2) - len(s1)):
            counter_window[s2[i]] -= 1
            counter_window[s2[i+len(s1)]] += 1
            if counter_window == counter_s1:
                return True
        
        return False