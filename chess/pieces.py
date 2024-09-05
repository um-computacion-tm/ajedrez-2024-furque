WHITE = 'White'
BLACK = 'Black'
symbolDictionary = {
    WHITE: {
        'Pawn': "♙",
        'Rook': "♖",
        'Knight': "♘",
        'Bishop': "♗",
        'King': "♔",
        'Queen': "♕"
    },
    BLACK: {
        'Pawn': "♟",
        'Rook': "♜",
        'Knight': "♞",
        'Bishop': "♝",
        'King': "♚",
        'Queen': "♛"
    }
}

rowDictionary = {
  "a": 0,
  "b": 1,
  "c": 2,
  "d": 3,
  "e": 4,
  "f": 5,
  "g": 6,
  "h": 7,
}

WHITE = 'White'
BLACK = 'Black'

class ChessPiece:
    def __init__(self, piece_type, color, position):
        self.type = piece_type
        self.color = color
        self.position = position
        self.symbol = symbolDictionary[self.color][self.type]
        self.previous_position = position

    def get_column(self):
        return self.position[0]

    def get_row(self):
        return self.position[1]

    def update_position(self, new_position):
        self.previous_position = self.position
        self.position = new_position

class Pawn(ChessPiece):
    def __init__(self, color, position):
        super().__init__("Pawn", color, position)
        self.has_moved = False

    def valid_moves(self, new_position):
        moves = []
        direction = 1 if self.color == WHITE else -1

        # Single square move
        if new_position[0] == self.get_column() and new_position[1] == self.get_row() + direction:
            moves.append(new_position)

        # Diagonal capture
        if abs(new_position[0] - self.get_column()) == 1 and new_position[1] == self.get_row() + direction:
            moves.append(new_position)

        # Double square move
        if not self.has_moved and new_position[0] == self.get_column() and new_position[1] == self.get_row() + 2 * direction:
            moves.append(new_position)

        return moves

class Rook(ChessPiece):
    def __init__(self, color, position):
        super().__init__("Rook", color, position)

    def valid_moves(self, new_position):
        moves = []
        if new_position[0] == self.get_column() or new_position[1] == self.get_row():
            moves.append(new_position)
        return moves

class Bishop(ChessPiece):
    def __init__(self, color, position):
        super().__init__("Bishop", color, position)

    def valid_moves(self, new_position):
        moves = []
        if abs(new_position[0] - self.get_column()) == abs(new_position[1] - self.get_row()):
            moves.append(new_position)
        return moves

class Queen(ChessPiece):
    def __init__(self, color, position):
        super().__init__("Queen", color, position)

    def valid_moves(self, new_position):
        return Rook(self.color, self.position).valid_moves(new_position) + \
               Bishop(self.color, self.position).valid_moves(new_position)

class Knight(ChessPiece):
    def __init__(self, color, position):
        super().__init__("Knight", color, position)

    def valid_moves(self, new_position):
        if (abs(new_position[0] - self.get_column()) == 2 and abs(new_position[1] - self.get_row()) == 1) or \
           (abs(new_position[0] - self.get_column()) == 1 and abs(new_position[1] - self.get_row()) == 2):
            return [new_position]
        return []

class King(ChessPiece):
    def __init__(self, color, position):
        super().__init__("King", color, position)

    def valid_moves(self, new_position):
        if abs(new_position[0] - self.get_column()) <= 1 and abs(new_position[1] - self.get_row()) <= 1:
            return [new_position]
        return []



