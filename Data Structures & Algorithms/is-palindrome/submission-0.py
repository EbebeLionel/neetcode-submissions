class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = "".join([c for c in s if c.isalnum()])
        clean_string = clean_string.lower()

        l,r = 0, len(clean_string) - 1
        while l <= r:
            if clean_string[l] != clean_string[r]:
                return False
            l += 1
            r -= 1

        return True