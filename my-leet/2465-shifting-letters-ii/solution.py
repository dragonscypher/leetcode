class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        d = [0] * n

        for st, e, dr in shifts:
            dl = 1 if dr == 1 else -1
            d[st] += dl
            if e + 1 < n:
                d[e + 1] -= dl

        for i in range(1, n):
            d[i] += d[i - 1]

        r = []
        for i, char in enumerate(s):
            shift = d[i] % 26
            r.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))

        return ''.join(r)
