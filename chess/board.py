from chess.pieces import King,Knight,Rook,Bishop,Pawn,Queen

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.place_pieces()

    def place_pieces(self):
        # Piezas blancas
        self.place_pieces(0, 'white', [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook])
        self.place_pieces_pawns(1, 'white')
        # Piezas negras
        self.place_pieces(7, 'black', [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook])
        self.place_pieces_pawns(6, 'black')

    def place_pieces(self, row, color, piece_types):
        for i, piece_type in enumerate(piece_types):
            piece = piece_type(i, row, color)
            self.place_piece(piece)

    def place_pieces_pawns(self, row, color):
        for i in range(8):
            pawn = Pawn(i, row, color)
            self.place_piece(pawn)

    def place_piece(self, piece):
        x, y = piece.get_position()
        self.board[y][x] = piece

    #Guarda la posicion actual en una vatiable, elimina la anterior y actualiza la pieza en su nueva posición
    def move_piece(self, piece, new_x, new_y):
        if piece.is_valid_move(new_x, new_y, self):
            old_x, old_y = piece.get_position()
            self.board[old_y][old_x] = None
            self.board[new_y][new_x] = piece
            piece.set_position(new_x, new_y)
            return True
        return False

    def promote_pawn(self, pawn, new_x, new_y, new_piece):
        old_x, old_y = pawn.get_position()
        self.board[old_y][old_x] = None
        self.board[new_y][new_x] = new_piece
        new_piece.set_position(new_x, new_y)

    def print_board(self):
        print("    A    B    C    D    E    F    G    H")
        print("  +---------------------------------------+")
        for i in range(8):
            print(f"{8 - i} |", end=" ")
            for j in range(8):
                piece = self.board[i][j]
                print(f"{piece.get_icon():<4}" if piece else ".   ", end=" ")
            print("|")
        print("  +---------------------------------------+")
        print("    A    B    C    D    E    F    G    H")

    def get_piece_at(self, x, y):
        return self.board[y][x]

    def get_position_from_notation(self, notation):
        col = ord(notation[0]) - ord('a')
        row = 8 - int(notation[1])
        return col, row
