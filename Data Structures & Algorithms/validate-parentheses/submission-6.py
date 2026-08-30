class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "}": "{", ")": "(", "]": "["
        }
        stack = []

        for ch in s:
            if ch in brackets:
                if stack and stack[-1] == brackets[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False
