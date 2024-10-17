class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        o={i:j for j,i in enumerate(order)}
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            ml=min(len(w1),len(w2))
            for j in range(ml):
                if w1[j]!=w2[j]:
                    if o[w1[j]]>o[w2[j]]:
                        return False
                    break
            else:
                if len(w1)>len(w2):
                    return False
        return True
