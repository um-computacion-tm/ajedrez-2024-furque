from pieces import Rook, Knight, Bishop, Queen, King, Pawn, WHITE, BLACK
from pieces import symbolDictionary as symbols

class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(8)] for _ in range(8)]
        self.columns = "abcdefgh"

    def display(self):
        print("  +" + "---+" * 8)
        for idx, row in enumerate(self.grid):
            print(f"{self.columns[idx]} | " + " | ".join(row) + " |")
            print("  +" + "---+" * 8)
        print("    1   2   3   4   5   6   7   8")

    def place_piece(self, piece):
        col, row = piece.get_column(), piece.get_row()
        self.grid[col][row] = piece.symbol

    def can_move(self, piece, target_pos):
        target_col, target_row = target_pos
        target_square = self.grid[target_col][target_row]

        if target_square == " ":
            return True
        for color, symbols_dict in symbols.items():
            if target_square in symbols_dict.values():
                return color != piece.color
        return False

    def move_piece(self, piece, target_pos):
        start_col, start_row = piece.get_column(), piece.get_row()
        target_col, target_row = target_pos

        if self.can_move(piece, target_pos):
            self.grid[start_col][start_row] = " "
            self.grid[target_col][target_row] = piece.symbol
            piece.update_position((target_col, target_row))
            return True
        return False

    def path_clear(self, piece, path):
        if isinstance(piece, Pawn):
            if len(path) == 1:
                col, row = path[0]
                straight_move = col == piece.get_column()
                return (self.grid[col][row] == " ") if straight_move else (self.grid[col][row] != " ")
            elif len(path) == 2:
                return all(self.grid[col][row] == " " for col, row in path)
            return False
        elif isinstance(piece, (Bishop, Queen, Rook)):
            return all(self.grid[col][row] == " " for col, row in path[:-1])
        return True
