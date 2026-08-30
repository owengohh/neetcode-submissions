class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        visited = set(nums)

        for num in visited:
            if num-1 not in visited:
                count = 1
                curr_num = num
                while curr_num + 1 in visited:
                    curr_num += 1
                    count += 1
                longest = max(longest, count)
        return longest