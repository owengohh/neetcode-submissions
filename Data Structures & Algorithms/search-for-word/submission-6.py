class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(board), len(board[0])

        def dfs(x, y, i):
            if i == len(word):
                return True
            if not (0 <= x < rows and 0 <= y  < cols) or board[x][y] != word[i]:
                return False
            temp_char = board[x][y] # Store original character
            board[x][y] = '#'
            for dx, dy in directions:
                if dfs(dx+x, dy+y, i+1):
                    return True
            board[x][y] = temp_char
            return False
                

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False