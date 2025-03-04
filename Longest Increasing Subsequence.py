from bisect import bisect_left

class Solution:
    def lis(self, arr):
        if not arr:
            return []
        
        # Tail array to store the smallest tail of all increasing subsequences with length i+1
        tails = []
        for num in arr:
            pos = bisect_left(tails, num)
            if pos < len(tails):
                tails[pos] = num
            else:
                tails.append(num)
        
        return len(tails)
