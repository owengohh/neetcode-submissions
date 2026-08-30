class Solution:
    def isValid(self, s: str) -> bool:
        map_ = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        for ch in s:
            if ch not in map_:
                stack.append(ch)
            else:
                if not stack or stack[-1] != map_[ch]:
                    return False
                stack.pop()
        
        return not stack