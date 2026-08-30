class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)  # front -> back
        stack = []  # times

        for p, s in cars:
            t = (target - p) / s
            stack.append(t)
            # if behind car catches up to fleet ahead, merge (pop)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)