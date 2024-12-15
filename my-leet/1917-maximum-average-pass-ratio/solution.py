class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        queue = sorted([(p, t) for p, t in classes], key = lambda x: ((x[1] - x[0]) / (x[1] * (x[1] + 1))))
        for i in range(extraStudents):
            p, t = queue.pop(-1)
            p, t = p + 1, t + 1
            bisect.insort(queue, (p, t), key = lambda x: ((x[1] - x[0]) / (x[1] * (x[1] + 1))))  
        return sum([p / t for p, t in queue]) / len(queue)
