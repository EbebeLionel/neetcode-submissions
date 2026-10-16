'''
{
')': '(',
']': '[',
'}': '{'
}

U
-Verify if parentheses are valid
-Input: string
-Output: boolean

[(, )]

pops )

if paren[)] in 

()

'([{'

MPIRE
'''

class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack or stack[-1] != matches[ch]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0
        