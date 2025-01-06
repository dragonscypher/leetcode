class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        n = len(boxes)
        count = x = 0
        for i in range(n):
            res.append(count)
            x += int(boxes[i])
            count += x

        count = x = 0
        for i in range(n - 1, -1, -1):
            res[i] += count
            x += int(boxes[i])
            count += x

        return res
