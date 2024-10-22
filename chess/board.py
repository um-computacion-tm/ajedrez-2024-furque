from chess.pieces import King, Knight, Rook, Bishop, Pawn, Queen

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.define_pieces()

    def define_pieces(self):
        # Coloca las piezas en sus posiciones iniciales
        self.place_pieces(0, 'white', [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook])
        self.place_pieces_pawns(1, 'white')  # Descomenta esta línea
        self.place_pieces(7, 'black', [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook])
        self.place_pieces_pawns(6, 'black')  # Descomenta esta línea

    def place_pieces(self, row, color, piece_types):
        # Coloca una fila específica de piezas (torres, caballos, etc.)
        for i, piece_type in enumerate(piece_types):
            piece = piece_type(i, row, color)
            self.place_piece(piece)

    def place_pieces_pawns(self, row, color):
        # Coloca los peones
        for i in range(8):
            pawn = Pawn(i, row, color)
            self.place_piece(pawn)

    def place_piece(self, piece):
        # Coloca una pieza en su posición en el tablero
        x, y = piece.get_position()
        self.board[y][x] = piece

    def move_piece(self, piece, new_x, new_y):
        # Verifica si hay una pieza en la posición destino
        target_piece = self.get_piece_at(new_x, new_y)
        
        if piece.is_valid_move(new_x, new_y, self):
            # Si hay una pieza en el destino y es del mismo color, el movimiento no es válido
            if target_piece and target_piece.get_color() == piece.get_color():
                return False
                
            # Realiza el movimiento
            old_x, old_y = piece.get_position()
            self.board[old_y][old_x] = None
            self.board[new_y][new_x] = piece
            piece.set_position(new_x, new_y)
            return True
        return False

    def print_board(self):
        # Imprime el tablero de ajedrez
        print("    A B C D E F G H")
        print("  +-----------------+")
        for i in range(8):
            print(f"{8 - i} |", end=" ")
            for j in range(8):
                piece = self.board[i][j]
                print(f"{piece.get_icon() if piece else '.'}", end=" ")
            print(f"| {8 - i}")
        print("  +-----------------+")
        print("    A B C D E F G H")

    def get_piece_at(self, x, y):
        if 0 <= x < 8 and 0 <= y < 8:  # Verifica que las coordenadas estén dentro del tablero
            return self.board[y][x]
        return None

    def get_position_from_notation(self, notation):
        if len(notation) != 2:
            raise ValueError("Notación inválida")
        
        notation = notation.lower()
        col = ord(notation[0]) - ord('a')  # Columna de 'a' a 'h'
        row = 8 - int(notation[1])         # Fila de 8 a 1
        
        if not (0 <= col < 8 and 0 <= row < 8):
            raise ValueError("Posición fuera del tablero")
            
        return col, row