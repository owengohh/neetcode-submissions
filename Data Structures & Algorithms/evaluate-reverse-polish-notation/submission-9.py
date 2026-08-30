class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in "-+/*":
                num2 = stack.pop()
                num1 = stack.pop()
                if t == '+':
                    stack.append(num1 + num2)
                if t == '-':
                    stack.append(num1 - num2)
                if t == '/':
                    stack.append(int(num1 / num2))
                if t == '*':
                    stack.append(num1 * num2)
            else:
                stack.append(int(t))
        
        return stack[-1]