class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []

        res = []
        digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz",
        }
        
        def bt(i, curr):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return

            for ch in digitToChar[digits[i]]:
                curr.append(ch)
                bt(i+1, curr)
                curr.pop()

        bt(0, [])
        print(res)
        return res