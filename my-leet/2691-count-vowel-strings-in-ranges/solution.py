class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        pre = [0] * (n + 1)
        v = set('aeiou')
        
        for i in range(n):
            pre[i + 1] = pre[i]
            if words[i][0] in v and words[i][-1] in v:
                pre[i + 1] += 1
        
        return [pre[r + 1] - pre[l] for l, r in queries]
