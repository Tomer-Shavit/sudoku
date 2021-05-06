class Sudoku:
    def __init__(self, board):
        self.board = board
        self.solved_board = [row[:] for row in board]

    def get_board(self):
        return self.board
    
    def set_board(self, board):
        self.board = board
        self.solved_board = board

    def print_original_board(self):
        self.print(self.board)

    def print_solved_board(self):
        self.print(self.solved_board)
    
    def print(self, board):
        """Receiving a matrix and printing a board with seperation"""
        for i in range(len(board)):
            if i % 3 == 0 and i!=0:
                print('---------------------------------')
            
            for j in range(len(board[i])):
                if j%3==0 and j!=0:
                    print(" | ", end='')
                print(" " + str(board[i][j]) + " ", end='')
            
            print('')


    def find_empty(self,board):
        """Receiving a matrix, loops through it, and return a tuple 
        with the row and the column of the free stop in the matrix"""
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==0:
                    return (i,j)
        return None


    def is_valid(self, board, num, pos):
        """Receiving matrix, a number we want to insert, and a tuple with the row and col
        and will check if the row, col, and box are valid so we can place the number 
        in the position"""

        # Check row
        for i in range(len(board[pos[0]])):
            if pos[0] != i and board[pos[0]][i] == num:
                return False
            
        # Check col
        for i in range(len(board)):
            if pos[1] != i and board[i][pos[1]] == num:
                return False

        pos_row = pos[0] // 3  
        pos_col = pos[1] // 3   
        
        for i in range(pos_row*3  ,pos_row*3 + 3):
            for j in range(pos_col * 3, pos_col*3 + 3):
                if (i,j) != pos and board[i][j] == num:
                    return False
        
        return True


    def solve(self):
        """Using backtracking algorithm to solve the solved_board variable"""
        find = self.find_empty(self.solved_board)

        if not find:
            return True
        else:
            row, col = find 
        
        for i in range(1,10):
            if(self.is_valid(self.solved_board, i, (row, col))):
                self.solved_board[row][col] = i

                if self.solve():
                    return self.solved_board
            
            self.solved_board[row][col] = 0
            
        return False





