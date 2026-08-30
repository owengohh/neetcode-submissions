class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y, i):
            if i == len(word):
                return True
            if not(0 <= x < rows and 0 <= y < cols):
                return False
            
            if board[x][y] != word[i]:
                return False

            tmp = board[x][y]

            board[x][y] = "#"
            
            for dx, dy in directions:
                if dfs(x+dx, y+dy, i+1):
                    return True
            
            board[x][y] = tmp
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False
                    