class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        ml = -1

        for l in range(1, n + 1):
            f = {}

            for i in range(n - l + 1):
                sub = s[i:i + l]

                if all(c == sub[0] for c in sub):
                    f[sub] = f.get(sub, 0) + 1
                    if f[sub] >= 3:
                        ml = max(ml, l)

        return ml
