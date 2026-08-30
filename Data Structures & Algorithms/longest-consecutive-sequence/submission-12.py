class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for num in nums:
            if num-1 in nums:
                continue
            curr_num = num
            curr_len = 1
            while curr_num + 1 in nums:
                curr_len += 1
                curr_num += 1
            longest = max(curr_len, longest)
        return longest