class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        a=sentence.split(" ")
        c=0
        for i in a:
            # i=list(i)
            # p=list(searchWord)
            
            if (i.startswith(searchWord)) and c<=1:
                c+=1
                return(a.index(i)+1)
            else:
                continue
        return -1
