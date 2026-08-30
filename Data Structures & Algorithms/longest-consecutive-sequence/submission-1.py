class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set(nums)
        longest = 0
        for num in visited:
            if num-1 not in visited:
                curr = num
                count = 1
                while curr+1 in visited:
                    count += 1
                    curr += 1
                longest = max(longest, count)
        return longest
                    