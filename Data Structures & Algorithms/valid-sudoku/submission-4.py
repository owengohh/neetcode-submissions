class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        for i in range(len(board)):
            row_set = set()
            col_set = set()
            for j in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] in row_set:
                        return False
                if board[j][i] != '.':
                    if board[j][i] in col_set:
                        return False
                row_set.add(board[i][j])
                col_set.add(board[j][i])
            

        start = [
            (0, 0), (3, 0), (6, 0),
            (0, 3), (3, 3), (6, 3),
            (0, 6), (3, 6), (6, 6)
        ]

        for x, y in start:
            box_set = set()
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if board[i][j] != ".":
                        if board[i][j] in box_set:
                            return False
                    box_set.add(board[i][j])
        
        return True