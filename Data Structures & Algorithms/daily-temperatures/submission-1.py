class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
            while stack and stack[-1][1] < curr_temp:
                idx, _ = stack.pop()
                res[idx] = i - idx 
            stack.append((i, curr_temp))
        
        return res
