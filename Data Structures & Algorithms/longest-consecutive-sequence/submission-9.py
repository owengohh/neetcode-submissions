class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set(nums)
        longest = 0

        for num in visited:
            if num-1 not in visited:
                count = 1
                curr_num = num
                while curr_num + 1 in visited:
                    count += 1
                    curr_num += 1
                print(count)
                longest = max(longest, count)
        return longest