class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check
        
        for row in board:
            seen=set()
            for ele in row:
                if ele=='.':
                    continue
                elif ele in seen:
                    return False
                else:
                    seen.add(ele)
        
        #column check

        for column in range(9):
            seen=set()
            for row in range(9):
                if board[row][column]=='.':
                    continue
                elif board[row][column] in seen:
                    return False
                else:
                    seen.add(board[row][column])
        
        #3x3 check
        
        for box_row in range(0,9,3):
            for box_column in range(0,9,3):
                seen=set()
                for row in range(3):
                    for column in range(3):
                        if board[row+box_row][column+box_column]=='.':
                            continue
                        elif board[row+box_row][column+box_column] in seen:
                            return False
                        else:
                            seen.add(board[box_row+row][box_column+column])
                            
        return True
        

        

        