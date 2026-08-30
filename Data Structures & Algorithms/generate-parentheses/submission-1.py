class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def bt(i, j, curr):
            if len(curr) == 2 * n:
                res.append("".join(curr))
            if i < n:
                curr.append("(")
                bt(i+1, j, curr)
                curr.pop()
            if j < i:
                curr.append(")")
                bt(i, j+1, curr)
                curr.pop()
        
        bt(0, 0, [])
        return res