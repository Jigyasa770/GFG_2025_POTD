import heapq

class Solution:
    def getMedian(self, arr):
        min_heap = []  # Min-heap for the right half (stores larger values)
        max_heap = []  # Max-heap for the left half (stores smaller values, negated for heapq)
        result = []
        
        for num in arr:
            # Insert into max heap (negate the number to simulate max heap)
            heapq.heappush(max_heap, -num)
            
            # Balance heaps: max_heap should have the smaller half, min_heap the larger half
            if max_heap and min_heap and (-max_heap[0] > min_heap[0]):
                val = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, val)
            
            # Ensure the size property is maintained
            if len(max_heap) > len(min_heap) + 1:
                val = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, val)
            elif len(min_heap) > len(max_heap):
                val = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -val)
            
            # Compute median
            if len(max_heap) > len(min_heap):
                result.append(float(-max_heap[0]))
            else:
                result.append(((-max_heap[0]) + min_heap[0]) / 2.0)
        
        return result
