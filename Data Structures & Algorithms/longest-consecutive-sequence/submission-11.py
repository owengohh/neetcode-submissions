class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set(nums)
        res = 0

        for num in visited:
            if num - 1 not in visited:
                curr_num = num
                curr_len = 1
                while curr_num + 1 in visited:
                    curr_len += 1
                    curr_num += 1
                res = max(curr_len, res)
        return res