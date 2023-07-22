import random


class Tic_Tac_Toe:
    def __init__(self) -> None:
        """Initialization function."""
        # Valid moves
        self.moves: list[str] = ["Rock", "Paper", "Scissors"]

        # What beats what. Key beats value.
        self.win_map: dict[str, str] = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper"
        }

        # Winning action message
        self.win_message: dict[str, str] = {
            "Rock": "smashes",
            "Paper": "covers",
            "Scissors": "slices"
        }

    def run(self) -> None:
        while True:
            computer: str = self.moves[random.randint(0, len(self.moves)-1)]
            move: str = self.get_move()
            self.check_winner(computer=computer, player=move)

    def get_move(self) -> str:
        while True:
            print("Options:", [f"{x}" for x in self.moves])
            move: str = input("Enter: ")
            if move.strip() in self.moves:
                break
            else:
                print("Invalid or mistyped move.")
        return move

    def check_winner(self, computer, player) -> None:
        if computer == player:
            print("Tie!")
        elif self.win_map[computer] == player:
            print(f"You lose, computer {self.win_message[computer]} you :(")
        else:
            print(f"You win! Your move {self.win_message[player]} the computer!")

def main() -> None:
    """Entry point for tic tac toe game."""
    game: Tic_Tac_Toe = Tic_Tac_Toe()

    game.run()

if __name__ == "__main__":
    main()