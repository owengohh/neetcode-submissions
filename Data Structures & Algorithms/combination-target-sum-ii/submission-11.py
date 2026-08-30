class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def bt(i, curr, remain):
            if remain == 0:
                res.append(curr[:])
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] > remain:
                    break
                curr.append(candidates[j])
                bt(j+1, curr, remain-candidates[j])
                curr.pop()
        
        bt(0, [], target)
        return res
