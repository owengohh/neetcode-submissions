class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def bt(i, curr):
            
            res.append(curr[:])
            for j in range(i, len(nums)):
                if j > i and nums[j-1] == nums[j]:
                    continue
                curr.append(nums[j])
                bt(j+1, curr)
                curr.pop()
                
        
        bt(0, [])
        return res
            