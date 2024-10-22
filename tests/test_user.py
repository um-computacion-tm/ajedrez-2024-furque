import unittest
from chess.pieces import King
from chess.user import user

class MockPiece:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

class MockKing(King, MockPiece):
    def __init__(self, color):
        # Pasar valores arbitrarios para x, y
        super().__init__(0, 0, color)

class MockBoard:
    def __init__(self, board):
        self.board = board

class TestUser(unittest.TestCase):

    def setUp(self):
        # Crear un tablero con diferentes piezas
        self.empty_board = MockBoard([
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]
        ])
        
        self.board_with_white_king = MockBoard([
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, MockKing('white'), None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]
        ])
        
        self.board_with_black_king = MockBoard([
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, MockKing('black'), None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]
        ])
        
        self.user_with_empty_board = user(self.empty_board)
        self.user_with_white_king = user(self.board_with_white_king)
        self.user_with_black_king = user(self.board_with_black_king)

    def test_has_king_with_empty_board(self):
        self.assertFalse(self.user_with_empty_board.has_king('white'))
        self.assertFalse(self.user_with_empty_board.has_king('black'))

    def test_has_king_with_white_king(self):
        self.assertTrue(self.user_with_white_king.has_king('white'))
        self.assertFalse(self.user_with_white_king.has_king('black'))

    def test_has_king_with_black_king(self):
        self.assertFalse(self.user_with_black_king.has_king('white'))
        self.assertTrue(self.user_with_black_king.has_king('black'))

    def test_has_pieces_with_empty_board(self):
        self.assertFalse(self.user_with_empty_board.has_pieces('white'))
        self.assertFalse(self.user_with_empty_board.has_pieces('black'))

    def test_has_pieces_with_white_king(self):
        self.assertTrue(self.user_with_white_king.has_pieces('white'))
        self.assertFalse(self.user_with_white_king.has_pieces('black'))

    def test_has_pieces_with_black_king(self):
        self.assertFalse(self.user_with_black_king.has_pieces('white'))
        self.assertTrue(self.user_with_black_king.has_pieces('black'))

if __name__ == '__main__':
    unittest.main()
