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

    def test_Dama_movimiento(self):
        self.assertTrue(self.white_queen.valid_moves('a4', self.board))
        self.assertEqual(self.white_queen.position, 'a4')
        
        self.assertFalse(self.white_queen.valid_moves('h6', self.board))
        self.assertEqual(self.white_queen.position, 'a4')
   
if __name__ == '__main__':
    unittest.main()
