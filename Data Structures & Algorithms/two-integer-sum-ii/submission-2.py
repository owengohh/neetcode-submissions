class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in numbers:
                return [i+1, numbers.index(diff)+1]