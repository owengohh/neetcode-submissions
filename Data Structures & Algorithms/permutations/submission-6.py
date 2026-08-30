class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    bt(curr)
                    curr.pop()

        bt([])
        return res