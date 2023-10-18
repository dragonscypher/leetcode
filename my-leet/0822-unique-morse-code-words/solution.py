class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
             "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
             "..-","...-",".--","-..-","-.--","--.."]
        
        transformations = set()
        
        for word in words:
            morse_word = ''.join([m[ord(char) - ord('a')] for char in word])
            transformations.add(morse_word)
            
        return len(transformations)

