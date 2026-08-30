class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y):
            if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] != 1:
                return 0
            grid[x][y] = 0
            area = 1
            for dx, dy in directions:
                area += dfs(x+dx, y+dy)
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area,area)
        
        return max_area