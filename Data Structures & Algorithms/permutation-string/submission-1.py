class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if m < n:
            return False

        need = defaultdict(int)
        for c in s1:
            need[c] += 1

        have = defaultdict(int)
        formed = 0
        l = 0

        for r in range(m):
            c = s2[r]
            have[c] += 1

            if c in need:
                if have[c] == need[c]:
                    formed += 1
                elif have[c] == need[c] + 1:
                    formed -= 1  # we just exceeded, so it's no longer "formed"

            while r - l + 1 > n:
                left = s2[l]
                if left in need:
                    if have[left] == need[left]:
                        formed -= 1  # leaving an exact match -> no longer formed
                    elif have[left] == need[left] + 1:
                        formed += 1  # was over, now becomes exact

                have[left] -= 1
                l += 1

            if formed == len(need) and (r - l + 1) == n:
                return True

        return False



        