class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        charToIndex = defaultdict(list) # key: char, value: list of index
        for i, char in enumerate(source):
            charToIndex[char].append(i)
        
        ans = 1
        i, prevIndex = 0, -1
        while i < len(target):
            char = target[i]
            if char in charToIndex:
                indices = charToIndex[char]
                nextIndex = bisect.bisect_right(indices, prevIndex)
                if nextIndex == len(indices):
                    prevIndex = -1
                    ans += 1
                else:
                    prevIndex = indices[nextIndex]
                    i += 1
            else:
                return -1
        return ans
