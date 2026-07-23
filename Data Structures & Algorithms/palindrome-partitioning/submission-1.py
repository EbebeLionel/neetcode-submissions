from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(start: int, curr: List[str]) -> None:
            if start == len(s):
                res.append(list(curr))
                return

            for end in range(start, len(s)):
                substring = s[start : end + 1]
                if is_palindrome(substring):
                    curr.append(substring)
                    backtrack(end + 1, curr)
                    curr.pop()

        backtrack(0, [])
        return res