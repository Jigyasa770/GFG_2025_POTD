from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        if n == 0 or k == 0:
            return []
        
        dq = deque()  # Deque to store indices of array elements
        result = []

        for i in range(n):
            # Remove elements not within the current window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Remove elements smaller than the current element
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            dq.append(i)

            # Add the maximum of the current window to the result
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result
