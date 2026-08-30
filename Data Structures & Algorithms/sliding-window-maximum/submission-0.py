class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        # deque stores indices of elements in nums,
        # such that nums[deque[0]] is the largest
        # and subsequent elements are in decreasing order.
        deque_monotonic = collections.deque()

        for i, num in enumerate(nums):
            # 1. Remove elements from the back of deque
            # if they are smaller than or equal to the current num.
            # This maintains the monotonic decreasing property.
            while deque_monotonic and nums[deque_monotonic[-1]] <= num:
                deque_monotonic.pop()

            # 2. Add the current element's index to the back of the deque.
            deque_monotonic.append(i)

            # 3. Remove the index from the front of the deque
            # if it's outside the current window.
            # The oldest element is at deque_monotonic[0].
            if deque_monotonic[0] == i - k:
                deque_monotonic.popleft()

            # 4. Once the window has k elements,
            # the maximum element for the current window is at
            # the index deque_monotonic[0].
            if i >= k - 1:
                res.append(nums[deque_monotonic[0]])

        return res

