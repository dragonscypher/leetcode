class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.lower()
        letters_only = ''.join([char for char in licensePlate if char.isalpha()])
        license_counter = Counter(letters_only)
        
        # Helper function to check if word can be constructed from licensePlate
        def can_construct(word_counter, license_counter):
            for char, count in license_counter.items():
                if word_counter[char] < count:
                    return False
            return True

        min_len = float('inf')
        result = None

        for word in words:
            word_counter = Counter(word)
            if can_construct(word_counter, license_counter):
                if len(word) < min_len:
                    min_len = len(word)
                    result = word

        return result
