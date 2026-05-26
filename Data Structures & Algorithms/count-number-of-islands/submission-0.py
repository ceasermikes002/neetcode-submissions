from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # ── Step 1: Handle empty grid edge case ──────────────────────────────────
        # If the input grid is empty, there are no islands to count.
        # if not grid or not grid[0]:
        #     return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        # ── Step 2: Define the DFS helper to sink connected land ──────────────────
        # We use DFS to traverse all 4-directionally connected '1's and turn them to '0's.
        def dfs(r: int, c: int) -> None:
            # Base Case: check if the current coordinates are out of bounds
            # or if the current cell is water ('0')
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            # Mark the current land cell as visited by "sinking" it to '0'
            # # This avoids using an extra O(M * N) visited set
            grid[r][c] = '0'
            
            # Recursively visit all 4 adjacent neighbors (down, up, right, left)
            dfs(r + 1, c)  # Move Down
            dfs(r - 1, c)  # Move Up
            dfs(r, c + 1)  # Move Right
            dfs(r, c - 1)  # Move Left

        # ── Step 3: Iterate through the grid and trigger DFS on new islands ──────
        # Scan every cell in the 2D grid to find unvisited land
        for r in range(rows):
            for c in range(cols):
                # If we find land ('1'), it marks the discovery of a new island
                if grid[r][c] == '1':
                    # Increment the total island count
                    island_count += 1
                    # Sink the entire connected island to prevent recounting its parts
                    dfs(r, c)
                    
        return island_count