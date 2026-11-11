'''
U
Input: array of strings, token
Output: Integer
Edge cases:
    len(tokens) < 3

Constraints:
    What do you do if combination cannot work?

["1","2","+","3","*","4","-"]

[]

Create dict called operations

M
-Stack
P
if len(tokens) < 3:
    return 0

initialize res to 0
set operations to a dict
set stack to empty array
for i in range(len(token)):
    if tokens[i] in "*-+/":
        push to stack
        if i - 1 > 0 and i - 2 >= 0:
            res = compute tokens[i - 1] operand tokens[i - 2]
        else:
            return 0

        pop every element out of stack
        push res to stack

    push tokens[i] to stack

if len(stack) is 1:
    return element in stack

else:
    return 0
IRE
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b) if b != 0 else "Error: Division by zero",
        }

        stack = []

        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()

                res = operations[token](a, b)

                stack.append(res)

            else:
                stack.append(int(token))

        return stack[0]
