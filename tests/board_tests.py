from chess.pieces import Pawn
from chess.board import Board
from chess.pieces import Queen
from chess.piece import Piece
from chess.piece import Piece
from chess.board import Board
import unittest


class boardtest(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.pawn = Pawn(1, 1, 'white')
        self.queen = Queen(3, 0, 'black')
        self.board.place_piece(self.pawn)
        self.board.place_piece(self.queen)

    def test_valid_move_pawn(self):
        result = self.board.move_piece(self.pawn, 1, 2)
        self.assertTrue(result)
        self.assertIsNone(self.board.board[1][1])
        self.assertEqual(self.board.board[2][1], self.pawn)

    def test_invalid_move_pawn(self):
        result = self.board.move_piece(self.pawn, 1, 8)
        self.assertFalse(result)
        self.assertEqual(self.board.board[1][1], self.pawn)


class boardproperties(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.pawn = Pawn(1, 1, 'white')
        self.board.place_piece(self.pawn)

    def test_get_piece_at(self):
        piece = self.board.get_piece_at(1, 1)
        self.assertEqual(piece, self.pawn)

    def test_get_piece_at_empty_square(self):
        piece = self.board.get_piece_at(0, 0)
        self.assertIsNone(piece)

    def test_get_position_from_notation(self):
        col, row = self.board.get_position_from_notation('a1')
        self.assertEqual((col, row), (0, 7))

        col, row = self.board.get_position_from_notation('h8')
        self.assertEqual((col, row), (7, 0))

        col, row = self.board.get_position_from_notation('d4')
        self.assertEqual((col, row), (3, 4))

    def test_print_board(self):
        self.board.print_board()

    def test_place_piece(self):
        board = Board()
        piece = Piece(0, 0, 'white') 
        board.place_piece(piece)
        self.assertEqual(board.get_piece_at(0, 0), piece)

    def test_place_multiple_pieces(self):
        board = Board()
        piece1 = Piece(0, 0, 'white')
        piece2 = Piece(7, 7, 'black')
        board.place_piece(piece1)
        board.place_piece(piece2)
        self.assertEqual(board.get_piece_at(0, 0), piece1)
        self.assertEqual(board.get_piece_at(7, 7), piece2)

    def test_get_piece_at_empty_square(self):
        board = Board()
        piece = board.get_piece_at(3, 3)
        self.assertIsNone(piece)


if __name__ == '__main__':
    unittest.main()
