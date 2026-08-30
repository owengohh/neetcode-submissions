class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(curr, count):
            if count == len(nums):
                res.append(curr[:])
                return
            curr.append(nums[count])
            bt(curr, count + 1)
            curr.pop()
            bt(curr, count + 1)
        
        bt([], 0)
        return res