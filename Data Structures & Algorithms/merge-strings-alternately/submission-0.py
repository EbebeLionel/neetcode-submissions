'''
U
-Input: word1 = "ab", word2 = "abbxxc"

Output: "aabbbxxc", pt1, pt2 = 0, 0
pt1 = 2, pt2 = 2

"ab"   "abbxxc"
  ^      ^
res = aabb

if pt1 < len(word1): return res + word1[pt1:]
elif pt2 < len(word2): return res + word2[pt2:]
 return res
M
-Two pointer problem
P
-initialize res to empty string
-initialize pt1 and pt2 to zero each
-set while loop such that it runs long as pt1 is less than len(word1) and pt2 is less than len(word2):
    -add word1[pt1] + word[pt2] in that order to res
    -pt1 += 1
    -pt2 += 1

if pt1 < len(word1):
    res += word1[pt1:]

- else same logic for pt2 as pt1

return res
IRE
'''


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        pt1, pt2 = 0, 0

        while pt1 < len(word1) and pt2 < len(word2):
            res += word1[pt1] + word2[pt2]
            pt1 += 1
            pt2 += 1
        
        if pt1 < len(word1):
            res += word1[pt1:]

        elif pt2 < len(word2):
            res += word2[pt2:]

        return res
