'''
U
-input: Array and integer
-output: List
-Edge case: nums is empty and k = 0
-Constraints?

nums = [1,2,2,3,3,3], k = 2

freq = {
    1: 1
    2: 2
    3: 3
}

[1,2,3]

MPIRE
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
            
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # heapq.nlargest on `freq` iterates over keys and compares using `freq.get`
        return heapq.nlargest(k, freq, key=freq.get)