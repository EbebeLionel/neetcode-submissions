'''
"ababd"
  l^r 
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""

        start, end = 0, 0
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return r - l - 1

        for i in range(len(s)):
            even = expand(i, i + 1)
            odd = expand(i, i)

            maxLen = max(even, odd)

            if maxLen > (end - start):
                start = i - (maxLen - 1) // 2
                end = i + maxLen // 2

        return s[start : end + 1]