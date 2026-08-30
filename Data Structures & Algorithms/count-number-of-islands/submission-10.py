class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(x, y):
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                grid[x][y] = '0'
                for dx, dy in directions:
                    dfs(dx+x, dy+y )

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        return count

            
