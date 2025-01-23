class Trie:

  def __init__(self, s):
    self.t = {}
    for i in range(len(s)):
      self.add(s[i:])

  def add(self, s):
    t = self.t
    for c in s:
      if c not in t:
        t[c] = {}
      
      t = t[c]
  


class Solution:

  def __init__(self):
    self.unique = set()

  def dfs(self, trie, cnt, stack):
    for c in trie.keys():
      cnt[c] = cnt.get(c, 0) + 1
      stack.append(c)

      val, is_ok = cnt[c], True
      for v in cnt.values():
        if v != val:
          is_ok = False
          break
          
      
      if is_ok:
        self.unique.add(''.join(stack))
      
      self.dfs(trie[c], cnt, stack)
      stack.pop()
      if cnt[c] == 1:
        del cnt[c]
      else:
        cnt[c] -= 1


  def equalDigitFrequency(self, s: str) -> int:
    t = Trie(s)
    self.dfs(t.t, {}, [])
    return len(self.unique)
    
