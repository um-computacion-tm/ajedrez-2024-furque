from pieces import Rook, Knight, Bishop, Queen, King, Pawn, WHITE, BLACK
from board import Board
from pieces import symbolDictionary as symbols
from pieces import rowDictionary as positions 

WHITE = 'White'
BLACK = 'Black'

class Game:
    def __init__(self, show_board=True):
        self.__board__ = Board()
        self.__current_turn__ = WHITE
        self.__first_turn_color__ = WHITE
        self.__second_turn_color__ = BLACK
        self.__game_over__ = False
        self.__pieces__ = []
        self.__move_count__ = 0
        self.__first_move__ = True
        self.__winner__ = None

    def initialize_pieces(self):  # Initializes pieces on the board and stores them in a list to determine the winning color later
        # White pieces
        self.__pieces__.extend([
            Rook(self.__first_turn_color__, (0, 0)), Rook(self.__first_turn_color__, (7, 0)),
            Knight(self.__first_turn_color__, (1, 0)), Knight(self.__first_turn_color__, (6, 0)),
            Bishop(self.__first_turn_color__, (2, 0)), Bishop(self.__first_turn_color__, (5, 0)),
            Queen(self.__first_turn_color__, (3, 0)), King(self.__first_turn_color__, (4, 0))
        ])

        self.__pieces__.extend([
            Pawn(self.__second_turn_color__, (0, 6)), Pawn(self.__second_turn_color__, (1, 6)),
        ])

    def place_pieces_on_board(self):
        for piece in self.__pieces__:
            self.__board__.place_piece(piece)

    def get_piece(self, position):  # Given a position, returns the piece at that position if the position is valid
        col, row = position
        for piece in self.__pieces__:
            if (piece.col == col and piece.row == row) and piece.color == self.__current_turn__:
                return piece
        return False

    def get_target_piece(self, position):
        col, row = position
        for piece in self.__pieces__:
            if (piece.col == col and piece.row == row) and piece.color == self.__current_turn__:
                return piece
        return False

    def move_piece(self, start_position, new_position):
        piece = self.get_piece(start_position)
        if not piece:
            return False
        start_col, start_row = start_position
        end_col, end_row = new_position
        target_piece = self.get_target_piece(new_position)
        path = piece.move_piece(new_position)
        if path and self.__board__.move_piece(piece, path) and self.__board__.place_piece(piece, new_position):
            self.__board__.place_piece(piece, new_position)
            if target_piece:
                self.__pieces__.remove(target_piece)

            self.__move_count__ += 1
            if isinstance(piece, Pawn):
                piece.has_moved = True
            return True
        else:
            piece.position((start_col, start_row))
            return False

    def process_input(self):
        coordinates = None
        while coordinates is None:
            coordinates = input("Enter move: ").replace(" ", "").strip()
            if coordinates == "exit":
                self.__game_over__ = True
                return False

            if self.validate_input(coordinates):
                first_letter = positions[coordinates[0].lower()]
                first_number = int(coordinates[1]) - 1
                second_letter = positions[coordinates[2].lower()]
                second_number = int(coordinates[3]) - 1
                return (first_letter, first_number), (second_letter, second_number)
            coordinates = None

    def validate_input(self, coordinates):
        try:
            coords = coordinates.replace(" ", "").lower()
            if len(coords) != 4:
                raise ValueError("Expected 2 coordinates (column and row)")
            letters, numbers = 'abcdefgh', '12345678'
            if (coords[0] not in letters or coords[2] not in letters or coords[1] not in numbers or coords[3] not in numbers):
                raise ValueError("Incorrect format")
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def determine_winner(self):  # Iterates over the board, and if one color has no pieces left, the other color wins
        white_pieces = False
        black_pieces = False

        for x in range(8):
            for y in range(8):
                piece = self.__board__.__board__[x][y]
                if piece in symbols[WHITE].values():
                    white_pieces = True
                elif piece in symbols[BLACK].values():
                    black_pieces = True

        if not black_pieces:
            return WHITE
        elif not white_pieces:
            return BLACK
        return None

    def take_turn(self):  # Determines if it's white's or black's turn based on the move count, and then calls process_game
        if self.determine_winner() is not None:
            self.__winner__ = self.determine_winner()
            self.__game_over__ = True

        if self.__move_count__ % 2 == 0:
            self.__current_turn__ = WHITE
        elif self.__move_count__ % 2 == 1:
            self.__current_turn__ = BLACK
        print(f"It's {self.__current_turn__}'s turn")
