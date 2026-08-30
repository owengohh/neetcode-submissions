class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            print(s[l], s[r])
            if not (s[l].isalpha() or s[l].isdigit()):
                l += 1
            elif not (s[r].isalpha() or s[r].isdigit()):
                r -= 1
            else:
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
        return True
