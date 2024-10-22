from chess.pieces import King

class user:
    def __init__(self, board):
        self.board = board

    # Comprueba si el jugador tiene un Rey en el tablero
    def has_king(self, color):
        return self.has_piece(color, King)  

    # Comprueba si un jugador tiene una pieza de un tipo específico en el tablero
    def has_piece(self, color, piece_type):
        for row in self.board.board:  
            if self.has_piece_in_row(row, color, piece_type):  
                return True
        return False  

    # Comprueba si una fila contiene una pieza del tipo y color especificado
    def has_piece_in_row(self, row, color, piece_type):
        for piece in row:  
            if self.is_piece_of_color(piece, color, piece_type):
                return True
        return False

    # Comprueba si un jugador tiene cualquier pieza en el tablero
    def has_pieces(self, color):
        for row in self.board.board:  
            if self.row_has_piece_of_color(row, color):
                return True
        return False

    # Comprueba si una fila tiene piezas del color especificado
    def row_has_piece_of_color(self, row, color):
        for piece in row:  
            if piece and piece.get_color() == color:  
                return True
        return False

    # Comprueba si una pieza es del tipo y color especificado
    def is_piece_of_color(self, piece, color, piece_type):
        return isinstance(piece, piece_type) and piece.get_color() == color
