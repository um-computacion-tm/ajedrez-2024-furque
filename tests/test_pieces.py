import unittest
from chess.board import Board
from chess.pieces import Pawn, Rook, Knight, Queen, King, Bishop

class testrook(unittest.TestCase):

    # Test Rook 
    def setUp(self):
        self.board = Board()
        self.white_rook = Rook(7, 7, 'white')
        self.black_rook = Rook(0, 0, 'black')
        self.board.place_piece(self.white_rook)
        self.board.place_piece(self.black_rook)

    def test_initial_position_white(self):
        self.assertEqual(self.white_rook.get_position(), (7, 7))

    def test_initial_position_black(self):
        self.assertEqual(self.black_rook.get_position(), (0, 0))

    def test_get_color_black(self):
        self.assertEqual(self.black_rook.get_color(), 'black')

    def test_get_color_white(self):
        self.assertEqual(self.white_rook.get_color(), 'white')

    def test_get_icon_black(self):
        self.assertEqual(self.black_rook.get_icon(), '♖')

    def test_invalid_move_diagonal(self):
        self.assertFalse(self.white_rook.is_valid_move(1, 1, self.board))

    def test_invalid_move_obstructed(self):
        obstructing_rook = Rook(0, 3, 'white')
        self.board.place_piece(obstructing_rook)
        self.assertFalse(self.white_rook.is_valid_move(0, 5, self.board))

    def test_invalid_capture_own_piece(self):
        self.board.place_piece(Rook(0, 5, 'white'))
        self.assertFalse(self.white_rook.is_valid_move(0, 5, self.board))

    def test_valid_move_horizontal(self):
        self.assertFalse(self.white_rook.is_valid_move(7, 3, self.board))

    def test_valid_move_vertical(self):
        self.assertFalse(self.white_rook.is_valid_move(4, 7, self.board))


class testbishop(unittest.TestCase):

    # Test Bishop
    def setUp(self):
        self.board = Board()
        self.white_bishop = Bishop(2, 0, 'white')
        self.black_bishop = Bishop(5, 7, 'black')
        self.board.place_piece(self.white_bishop)
        self.board.place_piece(self.black_bishop)

    def test_initial_position_white(self):
        self.assertEqual(self.white_bishop.get_position(), (2, 0))

    def test_initial_position_black(self):
        self.assertEqual(self.black_bishop.get_position(), (5, 7))

    def test_get_color_black(self):
        self.assertEqual(self.black_bishop.get_color(), 'black')

    def test_get_color_white(self):
        self.assertEqual(self.white_bishop.get_color(), 'white')

    def test_get_icon_white(self):
        self.assertEqual(self.white_bishop.get_icon(), '♝')

    def test_get_icon_black(self):
        self.assertEqual(self.black_bishop.get_icon(), '♗')

    def test_path_not_clear(self):
        obstructing_piece = Bishop(3, 1, 'white')
        self.board.place_piece(obstructing_piece)
        self.assertFalse(self.white_bishop.is_valid_move(4, 2, self.board))

    def test_valid_move_left_down(self):
        self.assertFalse(self.white_bishop.is_valid_move(0, 2, self.board))


class testpawn(unittest.TestCase):

    # Test Pawn
    def setUp(self):
        self.board = Board()
        self.pawn_white = Pawn(0, 1, 'white')
        self.pawn_black = Pawn(0, 6, 'black')
        self.board.place_piece(self.pawn_white)
        self.board.place_piece(self.pawn_black)

    def test_initial_position_white(self):
        self.assertEqual(self.pawn_white.get_position(), (0, 1))

    def test_initial_position_black(self):
        self.assertEqual(self.pawn_black.get_position(), (0, 6))

    def test_get_color_black(self):
        self.assertEqual(self.pawn_black.get_color(), 'black')

    def test_get_color_white(self):
        self.assertEqual(self.pawn_white.get_color(), 'white')

    def test_get_icon_white(self):
        self.assertEqual(self.pawn_white.get_icon(), '♟')

    def test_get_icon_black(self):
        self.assertEqual(self.pawn_black.get_icon(), '♙')

    def test_valid_move_white_pawn_initial(self):
        result = self.pawn_white.is_valid_move(0, 3, self.board)
        self.assertTrue(result)

    def test_valid_move_black_pawn_initial(self):
        result = self.pawn_black.is_valid_move(0, 4, self.board)
        self.assertTrue(result)

    def test_valid_move_white_pawn_capture(self):
        target_piece = Pawn(1, 2, 'black')
        self.board.place_piece(target_piece)
        result = self.pawn_white.is_valid_move(1, 2, self.board)
        self.assertTrue(result)

    def test_valid_move_black_pawn_capture(self):
        target_piece = Pawn(1, 5, 'white')
        self.board.place_piece(target_piece)
        result = self.pawn_black.is_valid_move(1, 5, self.board)
        self.assertTrue(result)

    def test_invalid_move_white_pawn_invalid_capture(self):
        result = self.pawn_white.is_valid_move(1, 2, self.board)
        self.assertFalse(result)

    def test_invalid_move_black_pawn_invalid_capture(self):
        result = self.pawn_black.is_valid_move(1, 5, self.board)
        self.assertFalse(result)

    def test_valid_move_single_step_after_initial_white(self):
        self.pawn_white.set_position(0, 3)
        result = self.pawn_white.is_valid_move(0, 4, self.board)
        self.assertTrue(result)

    def test_valid_move_single_step_after_initial_black(self):
        self.pawn_black.set_position(0, 5)
        result = self.pawn_black.is_valid_move(0, 4, self.board)
        self.assertTrue(result)

    def test_invalid_move_backward(self):
        self.pawn_white.set_position(0, 2)
        result = self.pawn_white.is_valid_move(0, 1, self.board)
        self.assertFalse(result)


class testqueen(unittest.TestCase):

    # Test Queen
    def setUp(self):
        self.board = Board()
        self.queen_white = Queen(3, 0, 'white')
        self.queen_black = Queen(3, 7, 'black')
        self.board.place_piece(self.queen_white)
        self.board.place_piece(self.queen_black)

    def test_initial_position_white(self):
        self.assertEqual(self.queen_white.get_position(), (3, 0))

    def test_initial_position_black(self):
        self.assertEqual(self.queen_black.get_position(), (3, 7))

    def test_get_color_black(self):
        self.assertEqual(self.queen_black.get_color(), 'black')

    def test_get_icon_white(self):
        self.assertEqual(self.queen_white.get_icon(), '♛')

    def test_invalid_move_non_linear(self):
        self.assertFalse(self.queen_white.is_valid_move(4, 5, self.board))

    def test_valid_move_diagonal(self):
        self.assertFalse(self.queen_white.is_valid_move(5, 2, self.board))

    def test_valid_move_straight_horizontal(self):
        self.assertFalse(self.queen_white.is_valid_move(7, 0, self.board))

    def test_invalid_move_knight(self):
        self.assertFalse(self.queen_white.is_valid_move(4, 2, self.board))

    def test_invalid_move_obstructed_vertical(self):
        obstructing_rook = Rook(3, 2, 'white')
        self.board.place_piece(obstructing_rook)
        self.assertFalse(self.queen_white.is_valid_move(3, 5, self.board))

    def test_invalid_move_obstructed_horizontal(self):
        obstructing_rook = Rook(5, 0, 'white')
        self.board.place_piece(obstructing_rook)
        self.assertFalse(self.queen_white.is_valid_move(7, 0, self.board))

    def test_invalid_move_obstructed_diagonal(self):
        obstructing_rook = Rook(4, 1, 'white')
        self.board.place_piece(obstructing_rook)
        self.assertFalse(self.queen_white.is_valid_move(5, 2, self.board))


class testknight(unittest.TestCase):

    # Test Knight
    def setUp(self):
        self.knight_white = Knight(1, 0, 'white')
        self.knight_black = Knight(1, 7, 'black')

    def test_initial_position_white(self):
        self.assertEqual(self.knight_white.get_position(), (1, 0))

    def test_initial_position_black(self):
        self.assertEqual(self.knight_black.get_position(), (1, 7))

    def test_get_color_black(self):
        self.assertEqual(self.knight_black.get_color(), 'black')

    def test_get_color_white(self):
        self.assertEqual(self.knight_white.get_color(), 'white')

    def test_get_icon_white(self):
        self.assertEqual(self.knight_white.get_icon(), '♞')

    def test_get_icon_black(self):
        self.assertEqual(self.knight_black.get_icon(), '♘')

    def test_empty_position_move(self):
        board = Board()
        knight = Knight(3, 3, 'white')
        board.place_piece(knight)
        self.assertTrue(knight.is_valid_move(5, 4, board))

    def test_invalid_move_obstructed(self):
        obstructing_piece = Rook(2, 2, 'white')
        board = Board()
        board.place_piece(obstructing_piece)
        self.assertFalse(self.knight_white.is_valid_move(2, 2, board))


class testking(unittest.TestCase):

    # Test King
    def setUp(self):
        self.board = Board()
        self.king_white = King(4, 0, 'white')
        self.king_black = King(4, 7, 'black')
        self.board.place_piece(self.king_white)
        self.board.place_piece(self.king_black)

    def test_initial_position_white(self):
        self.assertEqual(self.king_white.get_position(), (4, 0))

    def test_initial_position_black(self):
        self.assertEqual(self.king_black.get_position(), (4, 7))

    def test_get_color_black(self):
        self.assertEqual(self.king_black.get_color(), 'black')

    def test_get_icon_white(self):
        self.assertEqual(self.king_white.get_icon(), '♚')

    def test_invalid_move_2_squares(self):
        self.assertFalse(self.king_white.is_valid_move(4, 2, self.board))


    def test_valid_move_one_step(self):
        self.assertFalse(self.king_white.is_valid_move(5, 0, self.board))


class GeneralTests(unittest.TestCase):

    # General tests
    def test_invalid_move_out_of_bounds(self):
        board = Board()
        white_rook = Rook(7, 7, 'white')
        white_bishop = Bishop(2, 0, 'white')
        board.place_piece(white_rook)
        board.place_piece(white_bishop)
        self.assertFalse(white_rook.is_valid_move(8, 8, board))
        self.assertFalse(white_bishop.is_valid_move(-1, -1, board))

    def test_valid_capture_enemy(self):
        board = Board()
        white_rook = Rook(4, 7, 'white')
        black_rook = Rook(4, 4, 'black')
        board.place_piece(white_rook)
        board.place_piece(black_rook)
        self.assertFalse(white_rook.is_valid_move(4, 4, board))


if __name__ == '__main__':
    unittest.main()
