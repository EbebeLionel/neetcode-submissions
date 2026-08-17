'''
U
-Input: string, integer
-output: integer
-Example 1:
    -s = "XYYX", k = 2

    XYYX
       ^

    XXYYADC, k = 3
         ^
MPIRE
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        max_len = 0
        
        for right in range(len(s)):
            # Update frequency of the current character
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            
            # If valid replacements needed exceed k, shrink window from left
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            # Update maximum valid length found
            max_len = max(max_len, right - left + 1)
            '''
            XYYX
               ^
            count = {X: 2, Y: 2}
            r = 3
            l = 0
            freq = 2
            len = 4
            '''
        return max_len