'''
U
["act","pots","tops","cat","stop","hat"]

dict = {
"act" : ["act", "cat"]
"aht" : ["hat"]
"opst" : ["pots", "tops", "stop"]
}

Edge case: strs is empty
Constraints: Made up of lowercase English words

M
-Dictionary/ Hashing
P
-if strs is empty return [[]]
-initialize empty dictionary
-loop through every str
    -if sorted(str) is not in dict:
        -add sorted(str) and map it to [str]
    -else:
        -append str to sorted(str)
res = []
-for value in dict.values()
    -res.append(value)

-return res
IRE
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[]]

        my_dict = {}
        for s in strs:
            if "".join(sorted(s)) not in my_dict:
                my_dict["".join(sorted(s))] = [s]
            else:
                my_dict["".join(sorted(s))].append(s)

        res = []
        for value in my_dict.values():
            res.append(value)

        return res