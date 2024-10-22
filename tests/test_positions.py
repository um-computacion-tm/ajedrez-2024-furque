import unittest
from chess.piece import Piece
from chess.board import Board


class TestPiece(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.piece = Piece(4, 4, 'white')

    def test_get_position(self):
        self.assertEqual(self.piece.get_position(), (4, 4))

    def test_set_position(self):
        self.piece.set_position(2, 3)
        self.assertEqual(self.piece.get_position(), (2, 3))

    def test_get_color(self):
        self.assertEqual(self.piece.get_color(), 'white')

    def test_is_same_color_piece(self):
        other_piece = Piece(4, 5, 'white')
        self.board.place_piece(other_piece)
        self.assertTrue(self.piece.is_same_color_piece(4, 5, self.board))
        self.assertFalse(self.piece.is_same_color_piece(
            4, 3, self.board))

    def test_is_path_clear_vertical(self):
        blocking_piece = Piece(4, 6, 'white')
        self.board.place_piece(blocking_piece)
        self.assertFalse(self.piece.is_vertical_path_clear(7, self.board))
        self.assertTrue(self.piece.is_vertical_path_clear(5, self.board))

    def test_is_path_clear_horizontal(self):
        blocking_piece = Piece(6, 4, 'white')
        self.board.place_piece(blocking_piece)
        self.assertFalse(self.piece.is_horizontal_path_clear(7, self.board))
        self.assertTrue(self.piece.is_horizontal_path_clear(5, self.board))

    def test_is_path_clear_diagonal(self):
        blocking_piece = Piece(6, 6, 'white')
        self.board.place_piece(blocking_piece)
        self.assertFalse(self.piece.is_diagonal_path_clear(7, 7, self.board))
        self.assertTrue(self.piece.is_diagonal_path_clear(5, 5, self.board))

    def test_is_straight_move(self):
        self.assertTrue(self.piece.is_straight_move(4, 6))
        self.assertTrue(self.piece.is_straight_move(6, 4))
        self.assertFalse(self.piece.is_straight_move(5, 5))

    def test_is_diagonal_move(self):
        self.assertTrue(self.piece.is_diagonal_move(6, 6))
        self.assertFalse(self.piece.is_diagonal_move(5, 6)
                         )

    def test_check_move(self):
        self.assertTrue(self.piece.check_move(4, 6, self.board))
        blocking_piece = Piece(4, 6, 'white')
        self.board.place_piece(blocking_piece)
        self.assertFalse(self.piece.check_move(4, 6, self.board))


if __name__ == '__main__':
    unittest.main()
