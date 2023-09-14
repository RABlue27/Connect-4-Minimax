This is a simple implementation of the Connect 4 game in Python. It includes a game board, a player vs. AI mode, and a basic AI opponent. Below, you'll find a brief overview of the code and how to play the game.

# Code Structure

**game_board:** Represents the Connect 4 game board. It includes methods for making moves, checking for wins, printing the board, and evaluating the board's state.

**AI_agent:** Defines an AI agent that uses the minimax algorithm to make moves. It calculates the best move by searching to a specified depth in the game tree.

**game:** Manages the overall game, including player vs. AI interaction. It contains a game board and handles player input.

**main:** Initializes and starts the game.

# How to Play
Run the script.
The game starts with a printed game board.
Player 1 (you) is prompted to choose a column (1-7) to make a move. Enter a number and press Enter.
The game board is updated with your move. You'll be represented as 'X'.
Player 2 (AI) will make its move. The AI will be represented as 'O'.
The game continues in this alternating fashion until one player wins or the game ends in a tie.
Customization
You can customize the depth of the AI's search tree by modifying the DEPTH variable at the beginning of the code. A lower depth value will make the AI respond faster but may make it less strategic.

Have fun playing Connect 4!t
