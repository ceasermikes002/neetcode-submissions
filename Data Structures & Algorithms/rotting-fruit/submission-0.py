class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        #R,C are grid dimensions
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        #Initialize the queue and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c,0)) #Stre cell with time 0
                elif grid[r][c] == 1:
                    fresh_count += 1

        #Directions for adjacent cells
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        time_passed = 0

        #BFS to spread root
        while queue:
            r,c, time_passed = queue.popleft()
            for dr, dc in directions:
                rr, cc = r +dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == 1:
                    grid[rr][cc] = 2
                    fresh_count -= 1
                    queue.append((rr, cc, time_passed + 1))

        return time_passed if fresh_count == 0 else -1