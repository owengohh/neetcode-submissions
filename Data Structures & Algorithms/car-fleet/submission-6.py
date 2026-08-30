class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]:
            stack.append((p, s))
            if len(stack) > 1:
                p2, s2 = stack[-1]
                p1, s1 = stack[-2]

                if (target - p2) / s2 <= (target-p1) / s1:
                    stack.pop()

        return len(stack)