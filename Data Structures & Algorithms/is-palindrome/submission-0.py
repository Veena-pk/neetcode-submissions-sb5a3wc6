class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
        l = 0
        r = len(s_cleaned) - 1
        while l < r:
            if s_cleaned[l] == s_cleaned[r]:
                l += 1
                r -= 1
            else:
                return False
        return True