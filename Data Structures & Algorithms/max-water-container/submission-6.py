class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l <= r:
            min_height = min(heights[l], heights[r])
            area = min_height * (r-l)
            res = max(area, res)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return res