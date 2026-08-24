class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        sorted_s1 = ''.join(sorted(s1))

        while r <= len(s2):
            sliced = ''.join(sorted(s2[l:r]))
            if sliced == sorted_s1:
                return True
            l += 1
            r += 1
        return False