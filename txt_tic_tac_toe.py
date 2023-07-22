import random

class Tic_Tac_Toe:
    def __init__(self) -> None:
        """Initialization function."""
        # Setup the board
        self.board: list[list[str]] = [[" "] * 3, [" "] * 3, [" "] * 3]
        # If True, it is player's turn.
        self.turn: bool = True
        # Ends application when False
        self.is_running: bool = True

    def run(self) -> None:
        """Main function of class. Runs game loop."""
        while self.is_running:
            # Play turn
            if self.turn:
                self.display_board_to_terminal()
                self.play_user_move()                  
            else:
                self.play_computer_move()
            
            # Check for win
            if self.check_for_win(self.board):
                self.display_board_to_terminal()
                if self.turn:
                    print("Player wins!")
                else:
                    print("Computer wins!")
                self.is_running = False
            self.turn = not self.turn

    def display_board_to_terminal(self) -> None:
        """Prints the board to terminal."""
        print(" --- --- --- ")
        for i in range(len(self.board)):
            print("|", end=" ")
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=" ")
                print("|", end=" ")
            print("\n --- --- --- ")

    def play_user_move(self) -> None:
        """Gets input from player, places move on board."""
        move: tuple[int, int] = self.get_user_move()
        self.place_move_on_board(move=move, char='O')

    def play_computer_move(self) -> None:
        """Gets move from computer, places move on board."""
        while True:
            move: tuple[int, int] = (random.randint(0, 2), random.randint(0, 2))
            if self.is_valid_move(board=self.board, move=move):
                self.place_move_on_board(move=move, char='X')
                return

    def get_user_move(self) -> tuple[int, int]:
        """
        Prints options to player, gets input and validates move.
        If valid move, return move.
        """
        while True:
            print("Input move in format x,y (ex: 1,1 would be first space).")
            move = input("Enter: ")
            try:
                m = move.strip().split(",")
                result: tuple[int, int] = (int(m[0])-1, int(m[1])-1)
                if self.is_valid_move(board=self.board, move=result):
                    return result
            except:
                pass
            print("MOVE INVALID")

    def place_move_on_board(self, move: tuple[int, int], char: str) -> None:
        """Adds move to board."""
        self.board[move[1]][move[0]] = char

    @staticmethod
    def is_valid_move(board: list[list[str]], move: tuple[int,int]) -> bool:
        """
        Checks if input move is valid on input board. Checks for positive
        integers as well as there not already being a move places there.
        """
        if board[move[1]][move[0]] == " " and move[0] >= 0 and move[1] >= 0:
            return True
        return False
    
    @staticmethod
    def check_for_win(board: list[list[str]]) -> bool:
        # Check horizontal
        for i in range(len(board)):
            if board[i][0] != " " and board[i][0] == board[i][1] and board[i][0] == board[i][2]:
                return True
        # Check vertical
        for i in range(len(board)):
            if board[0][i] != " " and board[0][i] == board[1][i] and board[0][i] == board[2][i]:
                return True
        # Check diags
        if board[0][0] != " " and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
                return True
        if board[2][0] != " " and board[2][0] == board[1][1] and board[2][0] == board[0][2]:
                return True
        return False

if __name__ == "__main__":
    game: Tic_Tac_Toe = Tic_Tac_Toe()

    game.run()