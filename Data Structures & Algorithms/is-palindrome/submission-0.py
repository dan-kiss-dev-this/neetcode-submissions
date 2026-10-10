class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove not alpha numerica .isalnum()
        lower = s.lower()
        output = ''
        for c in lower:
            if c.isalnum():
                output += c
        reversed = output[::-1]
        if reversed == output:
            return True
        return False