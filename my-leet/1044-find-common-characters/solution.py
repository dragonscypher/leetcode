class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize reference count with the character frequencies of the first word
        ref_count = [0] * 26
        for ch in words[0]:
            ref_count[ord(ch) - ord('a')] += 1

        # For each subsequent word, update the reference count to the minimum
        # frequency of each character seen so far
        for word in words[1:]:
            current_count = [0] * 26
            for ch in word:
                current_count[ord(ch) - ord('a')] += 1
            for i in range(26):
                ref_count[i] = min(ref_count[i], current_count[i])

        # Convert the reference count back into a list of characters
        result = []
        for i, count in enumerate(ref_count):
            result.extend([chr(i + ord('a'))] * count)

        return result

