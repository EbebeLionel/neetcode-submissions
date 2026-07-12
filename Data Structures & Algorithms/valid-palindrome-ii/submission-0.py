class Solution:
    def validPalindrome(self, s: str) -> bool:
        cleaned_string = "".join(c.lower() for c in s if c.isalnum())
        cleaned_string = cleaned_string.lower()
        def validRoute(left, right):
            while left <= right:
                if cleaned_string[left] != cleaned_string[right]:
                    return False
                left += 1
                right -= 1

            return True

        l, r = 0, len(cleaned_string) - 1

        while l <= r:
            if cleaned_string[l] != cleaned_string[r]:
                return validRoute(l + 1, r) or validRoute(l, r - 1)

            l += 1
            r -= 1

        return True