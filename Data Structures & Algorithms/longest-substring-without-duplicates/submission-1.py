'''
U
-Input: string
-output: integer
-Edgecase:
    -No string

-Constraint:
    -
M
-Sliding window
P
-if not string return 0
-initialize start index = 0
-initialize maxCount equal to 0
-while loop as long as s less than length of string:
    -initialize seen set
    -initialize f equal to s
    -initialize count
        -while f is less than length of string and string[f] not in seen:
            -incremet count
            -increment f
            -add to set

        -maxCount is max between count and maxCount
        -increment s
IRE
s = "zxyzxyz"
zxyzxyz
 s
    f

seen = ()
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLen = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen

        