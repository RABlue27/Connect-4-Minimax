import math
import copy

# Variable to define max depth of our search
# Takes about 6 seconds to find a move at worst. Lower numbers will be quicker.
DEPTH = 5

#Create connect 4 game board
class game_board:
    def __init__(self):
        self.board = [['_' for i in range(7)] for j in range(6)]
        self.moves = 0
        self.max_moves = 7*6

    #Returns true on a valid move 
    def make_move(self, x, player):
        symbol = 'X' if player == 1 else 'O'
        if self.board[0][x] == '_':
            for i in range(5, -1, -1):
                if self.board[i][x] == '_':
                    self.board[i][x] = symbol
                    return True
        else:
            return False

    # Fuction to neatly print the board 
    def print_board(self):
        print("1 2 3 4 5 6 7")
        for i in range(6):
            for j in range(7):
                print(self.board[i][j], end=' ')
            print()
        print("\n")

    #Methods to check connect 4 wins on a 6x7 board
    def horizontal_win(self):
        for i in range(6):
            for j in range(4):
                if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3] and self.board[i][j] != '_':
                    return True
        return False

    def vertical_win(self):
        for i in range(3):
            for j in range(7):
                if self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j] and self.board[i][j] != '_':
                    return True
        return False

    def right_diagonal_win(self):
        for i in range(3):
            for j in range(4):
                if self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3] and self.board[i][j] != '_':
                    return True
        return False

    def left_diagonal_win(self):
        for i in range(3):
            for j in range(3, 7):
                if self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3] and self.board[i][j] != '_':
                    return True
        return False


    # Function to return a list of possible moves.Since make_move returns false on invalid move.
    def get_possible_moves(self):
        moves = []
        current_board = copy.deepcopy(self)
        for i in range(7):
            if current_board.make_move(i, 1):
                moves.append(i)
        return moves

    # Returns the heuristic value of the board. Sums all the winning and losing moves. 
    # Simpler heuristics prodiuced better results for me. 
    def evaluate(self):
        x = 0
        for i in range(6):
            for j in range(4):
                if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3] and self.board[i][j] == 'O':
                    x += 100
                if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3] and self.board[i][j] == 'X':
                    x-= 100
        for i in range(3):
            for j in range(7):
                if self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j] and self.board[i][j] == 'O':
                    x += 100
                if self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j] and self.board[i][j] == 'X':
                    x -= 100
        for i in range(3):
            for j in range(4):
                if self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3] and self.board[i][j] == 'O':
                    x += 100
                if self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3] and self.board[i][j] == 'X':
                    x -= 100
        for i in range(3):
            for j in range(3, 7):
                if self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3] and self.board[i][j] == 'O':
                    x += 100
                if self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3] and self.board[i][j] == 'X':
                    x -= 100      
 
        return x
    
    
# Class to define minimax algorithm
class AI_agent():
    def __init__(self, depth):
        self.depth = depth

    # Minimax function to a certain depth. 
    def minimax(self, depth, maximizing, board):
        temp = copy.deepcopy(board)
        if depth == 0 or temp.horizontal_win() or temp.vertical_win() or temp.right_diagonal_win() or temp.left_diagonal_win():
            return temp.evaluate()
        if maximizing:
            best_value = -math.inf
            for i in temp.get_possible_moves():
                temp.make_move(i, 2)
                value = self.minimax(depth-1, False, temp)
                best_value = max(best_value, value)
            return best_value
        else:
            best_value = math.inf
            for i in temp.get_possible_moves():
                temp.make_move(i, 1)
                value = self.minimax(depth-1, True, temp)
                best_value = min(best_value, value)
            return best_value
        
    # Calls the minimax function for each possible move and returns the best move. 
    def get_move(self, board):
        best_value = -math.inf
        best_move = None
        for i in board.get_possible_moves():
            temp = copy.deepcopy(board)
            temp.make_move(i, 2)
            value = self.minimax(self.depth, False, temp)
            if value > best_value:
                best_value = value
                best_move = i
        return best_move


class game():
    def __init__(self):
        self.board = game_board()
        self.player = 1

    def play(self):
        while True:
            self.board.print_board()
            # Player 1
            self.board.make_move(int(input('Player 1, choose a column: ')) -1 , 1)
            if self.board.horizontal_win() or self.board.vertical_win() or self.board.right_diagonal_win() or self.board.left_diagonal_win():
                self.board.print_board()
                print('Player 1 wins!')
                break
            if self.board.moves == self.board.max_moves:
                print('Tie!')
                break
            # AI player
            self.board.print_board()
            # AI / Player 2 goes
            print("Player 2 is thinking...")
            # Create an AI agent with depth of whatever we want. 
            AIagent = AI_agent(DEPTH)
            # Have AI agent make the move with the current given board state.
            move = AIagent.get_move(self.board)
            # Make a move on the board.
            self.board.make_move(move, 2)
            if self.board.horizontal_win() or self.board.vertical_win() or self.board.right_diagonal_win() or self.board.left_diagonal_win():
                self.board.print_board()
                print('Player 2 wins!')
                break
            if self.board.moves == self.board.max_moves:
                print('Tie!')
                break
            # Loop continuies until game is over.

class main():
    game = game()
    game.play()
