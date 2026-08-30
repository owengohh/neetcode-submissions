class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "+-*/"

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if t == "+":
                    stack.append(n1 + n2)
                if t == '-':
                    stack.append(n1 - n2)
                if t == "*":
                    stack.append(n1 * n2)
                if t == "/":
                    stack.append(int(n1 / n2))
        
        return stack[-1]