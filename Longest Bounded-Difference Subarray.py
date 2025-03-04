from collections import deque

class Solution:
    def longestSubarray(self, arr, x):
        min_deque = deque()  # To maintain the minimum values
        max_deque = deque()  # To maintain the maximum values
        left = 0
        max_len = 0
        start_index = 0
        
        for right in range(len(arr)):
            # Maintain the max deque
            while max_deque and arr[max_deque[-1]] <= arr[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Maintain the min deque
            while min_deque and arr[min_deque[-1]] >= arr[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Check the difference between max and min
            while arr[max_deque[0]] - arr[min_deque[0]] > x:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Update max_len and start_index
            if right - left + 1 > max_len:
                max_len = right - left + 1
                start_index = left
        
        return arr[start_index:start_index + max_len]
