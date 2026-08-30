class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = [ele for row in matrix for ele in row]
        l, r = 0, len(flat) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if target == flat[mid]:
                return True
            elif target > flat[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False