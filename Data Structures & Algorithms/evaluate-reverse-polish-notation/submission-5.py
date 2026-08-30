class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in '+-*/':
                n2 = stack.pop()
                n1 = stack.pop()
                if t == "+":
                    stack.append(n2 + n1)
                if t == '-':
                    stack.append(n1 - n2)
                if t == '*':
                    stack.append(n1 * n2)
                if t == '/':
                    stack.append(int(n1 / n2))
            else:
                stack.append(int(t))
            print(stack)
        
        return stack[-1]
        