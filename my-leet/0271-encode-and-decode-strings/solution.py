class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        e=""
        for a in strs:
            e+= str(len(a)) + "#" +a
        return e
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        d=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!= '#':
                j+=1
            l= int(s[i:j])
            i=j+1
            j=i+l
            d.append(s[i:j])
            i=j
        return d

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
