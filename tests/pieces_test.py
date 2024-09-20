import unittest
from chess.board import Board
from chess.pieces import Pawn, Rook, Knight, Queen, King, Bishop, BLACK, WHITE

class testpieces(unittest.TestCase):

    def setUp(self):
        # Create board with pieces for tests
        self.board = Board()
        self.white_king = King(WHITE, 'e1', self.board)
        self.white_queen = Queen(WHITE, 'd1', self.board)
        self.white_bishop = Bishop(WHITE, 'c1', self.board)
        self.white_knight = Knight(WHITE, 'b1', self.board)
        self.white_rook = Rook(WHITE, 'a1', self.board)
        self.white_pawn = Pawn(WHITE, 'e2', self.board)
        self.black_pawn = Pawn(BLACK, 'f5', self.board)
      
    def test_kingmovement(self):
        # tests that king can move in every direction but only one place.
        self.assertTrue(self.white_king.valid_moves('f2'))
        self.assertEqual(self.white_king.position, 'd2')
        self.assertFalse(self.white_king.valid_moves('h4'))    

    def test_queenmovement(self):
        self.assertTrue(self.white_queen.valid_moves('a4', self.board))
        self.assertEqual(self.white_queen.position, 'a4')
        
        self.assertFalse(self.white_queen.valid_moves('h6', self.board))
        self.assertEqual(self.white_queen.position, 'a4')

    def test_rook_verticalmove(self):
        self.assertTrue(self.white_rook.valid_moves('a1', self.board))
        self.assertEqual(self.white_rook.position, 'a3')
        
        self.assertFalse(self.white_rook.valid_moves('a1', self.board))
        self.assertEqual(self.white_rook.position, 'b1')

    def test_rook_horizontalmove(self):
        self.assertTrue(self.white_rook.valid_moves('a1', self.board))
        self.assertEqual(self.white_rook.position, 'b1')
        
        self.assertFalse(self.white_rook.valid_moves('a1', self.board))
        self.assertEqual(self.white_rook.position, 'a2')  
   
    def test_knightmove(self):
        self.assertTrue(self.white_knight.valid_moves('b1', self.board))
        self.assertEqual(self.white_knight.position, 'd3')

        self.assertFalse(self.white_knight.valid_moves('b1'))
        self.assertEqual(self.white_knight.position, 'b2')

    def test_pawnmove(self):
        self.assertTrue(self.white_pawn.valid_moves('d1', self.board))
        self.assertEqual(self.white_pawn.position, 'd2')

        self.assertFalse(self.white_pawn.valid_moves('b1'))
        self.assertEqual(self.white_pawn.position, 'b2')

    def test_blackpawn(self):
        self.assertTrue(self.black_pawn.valid_moves('d7', self.board))
        self.assertEqual(self.black_pawn.position, 'd8')

        self.assertFalse(self.black_pawn.valid_moves('b1'))
        self.assertEqual(self.black_pawn.position, 'b2')

if __name__ == '__main__':
    unittest.main()
