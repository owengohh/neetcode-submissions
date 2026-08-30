class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []

        for ch in s:
            if ch in p_map:
                if stack and stack[-1] == p_map[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return True if not stack else False