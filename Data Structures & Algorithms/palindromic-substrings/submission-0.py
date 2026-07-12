'''
s = "abc"
       ^
s = "aaa"
      ^^
s = "aaaa"
       ^^
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        def expand(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            return count

        total_palindromes = 0

        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)

            total_palindromes += odd + even

        return total_palindromes