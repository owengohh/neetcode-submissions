class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_count = 0
        num_set = set(nums)
        for i, num in enumerate(nums):
            if num - 1 not in num_set:
                curr_num = num
                curr_count = 1
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_count += 1
                
                longest_count = max(longest_count, curr_count)
        
        return longest_count