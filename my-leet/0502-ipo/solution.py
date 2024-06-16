import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if not profits or not capital or k == 0:
            return w
        
        # Create a list of projects with (capital, profit)
        projects = sorted(zip(capital, profits))
        
        max_profit_heap = []
        current_project = 0
        
        for _ in range(k):
            # Push all the projects that can be started with the current capital to the max heap
            while current_project < len(projects) and projects[current_project][0] <= w:
                heapq.heappush(max_profit_heap, -projects[current_project][1])
                current_project += 1
            
            # If no projects can be started, break the loop
            if not max_profit_heap:
                break
            
            # Pop the project with the maximum profit
            w -= heapq.heappop(max_profit_heap)
        
        return w

