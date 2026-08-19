'''
U
-Aim: Verify if s1 has as a permutation in s2
-Input: 2 strs
-Output: Bool
-Edge case:
    -no s1 and/or no s2

-Constraints:
    -1 <= s1.length, s2.length <= 10000

-s1 = "abc", 
-"lecabee"
       s
       f


  seen = (c, a, b)
  if len(seen) == len(s1):
    return True


  conditions: c in s1 and c not in seen
  seen set to track characters in s1 found in s2
M
-Sliding window
P
-if not s1 or not s2:
    -return False

-slow = 0
-while loop as long as slow < len(s2):
    -initialize seen empty set
    -initialize fast to slow
    -while s2[fast] in s1 and s2[fast] not in seen and fast < len(s2):
        -add s2[fast] to seen
        -increment fast

    -if len(seen) == len(s1):
        return True

    slow = fast

-return False
IRE
'''
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''if not s1 or not s2:
            return False

        slow = 0

        while slow < len(s2):
            fast = slow
            seen = set()

            while fast < len(s2) and s2[fast] in s1 and s2[fast] not in seen:
                seen.add(s2[fast])
                fast += 1

            if len(s1) == len(seen):
                return True

            slow += 1

        return False'''
        if not s1 or not s2:
            return False

        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        s1_counts = Counter(s1)
        window_counts = Counter(s2[:n1])

        if window_counts == s1_counts:
            return True

        for i in range(n1, n2):
            window_counts[s2[i]] += 1

            left_char = s2[i - n1]
            window_counts[left_char] -= 1
            if window_counts[left_char] == 0:
                del window_counts[left_char]

            if window_counts == s1_counts:
                return True

        return False


