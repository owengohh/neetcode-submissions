class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                index, h = stack.pop()
                max_area = max(max_area, h * (i-index))
                start = index
            stack.append((start, height))
        
        for i in range(len(stack)):
            idx, h = stack.pop()
            max_area = max(max_area, h * (len(heights)-idx))
        
        return max_area
