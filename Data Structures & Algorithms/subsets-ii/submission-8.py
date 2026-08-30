class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(index, current_subset):
            res.append(current_subset[:]) # Add current subset to results

            for i in range(index, len(nums)):
                # Skip duplicates
                if i > index and nums[i] == nums[i-1]:
                    continue

                current_subset.append(nums[i]) # Make a choice
                backtrack(i + 1, current_subset) # Explore
                current_subset.pop() # Undo the choice (backtrack)

        backtrack(0, [])
        return res