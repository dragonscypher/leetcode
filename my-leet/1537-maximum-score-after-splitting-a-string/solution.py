class Solution:
  def maxScore(self, s: str) -> int:
    a = 0
    z = 0
    o = s.count('1')
    for i in range(len(s) - 1):
      if s[i] == '0':
        z += 1
      else:
        o -= 1
      a = max(a, z + o)
    return a
