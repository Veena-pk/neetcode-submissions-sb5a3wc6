class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        l, r = 0, n
        s1_sorted = sorted(s1)

        while r <= len(s2):
            if sorted(s2[l:r]) == s1_sorted:
                return True
            else:
                l += 1
                r += 1
        
        return False