class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted = ""
        for c in s:
            if c.isalnum():
                converted += c.lower()
        if converted == converted[::-1]:
            return True
        return False
        # remove not alpha numerica .isalnum()
        # lower = s.lower()
        # output = ''
        # for c in lower:
        #     if c.isalnum():
        #         output += c
        # reversed = output[::-1]
        # print(output)
        # print(output[::-1])
        # if reversed == output:
        #     return True
        # return False