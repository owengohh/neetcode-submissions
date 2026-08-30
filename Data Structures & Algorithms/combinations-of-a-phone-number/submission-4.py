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
            if i == len(digits):
                res.append(curr)
                return
            
            for char in digitToChar[digits[i]]:
                curr += char
                bt(i+1, curr)
                curr = curr[:-1]
        
        bt(0, "")
        return res
