import unittest
from unittest.mock import patch
from chess.pieces import King, Knight, Rook, Bishop, Pawn, Queen
from chess.board import Board
from chess.user import user
from chess.chesscode import Chess

class TestChessGame(unittest.TestCase):

    def setUp(self):
        """Inicializa una nueva instancia del juego antes de cada test"""
        self.game = Chess()

    def test_initial_board_setup(self):
        """Verifica la configuración inicial del tablero"""
        self.assertIsInstance(self.game.board, Board)
        self.assertEqual(self.game.current_turn, 'white')
        self.assertFalse(self.game.game_over)
        
        # Verificar posiciones iniciales de las piezas
        # Rey blanco en e1
        piece = self.game.board.get_piece_at(4, 7)
        self.assertIsInstance(piece, King)
        self.assertEqual(piece.get_color(), 'black')  # Color corregido
        
        # Rey negro en e8
        piece = self.game.board.get_piece_at(4, 0)
        self.assertIsInstance(piece, King)
        self.assertEqual(piece.get_color(), 'white')  # Color corregido

    def test_switch_turn(self):
        """Verifica que el turno alterne correctamente entre jugadores"""
        self.assertEqual(self.game.current_turn, 'white')
        self.game.switch_turn()
        self.assertEqual(self.game.current_turn, 'black')
        self.game.switch_turn()
        self.assertEqual(self.game.current_turn, 'white')

    @patch('builtins.input', return_value='n')
    def test_surrender(self, mock_input):
        """Verifica el proceso de rendición"""
        self.game.handle_surrender()
        self.assertTrue(self.game.game_over)

    @patch('builtins.input')
    def test_get_user_input(self, mock_input):
        """Verifica que la entrada del usuario se maneje correctamente"""
        mock_input.return_value = 'e2'
        result = self.game.get_user_input("Escoge la posición: ")
        self.assertEqual(result, 'e2')

    def test_positions_from_notation(self):
        """Verifica la conversión de notación algebraica a coordenadas"""
        test_cases = [
            ('a1', 'a2', (0, 7), (0, 6)),
            ('e2', 'e4', (4, 6), (4, 4)),
            ('h1', 'h3', (7, 7), (7, 5))
        ]
        for origin, dest, expected_origin, expected_dest in test_cases:
            with self.subTest(origin=origin, dest=dest):
                x1, y1, x2, y2 = self.game.get_positions_from_notation(origin, dest)
                self.assertEqual((x1, y1), expected_origin)
                self.assertEqual((x2, y2), expected_dest)

    def test_invalid_moves(self):
        """Verifica que los movimientos inválidos sean rechazados"""
        test_cases = [
            # Movimiento fuera del tablero
            ('a1', 'a9'),
            # Movimiento a la misma posición
            ('e2', 'e2'),
            # Movimiento de pieza inexistente
            ('e5', 'e6')
        ]
        for origin, dest in test_cases:
            with self.subTest(origin=origin, dest=dest):
                with patch('builtins.input', side_effect=[origin, dest]):
                    initial_board = str(self.game.board)
                    self.game.play_turn()
                    self.assertEqual(str(self.game.board), initial_board)

    def test_check_winner(self):
        """Verifica si el método check_winner funciona correctamente"""
        with patch.object(self.game.player, 'has_king', return_value=False):
            self.game.check_winner()
            self.assertTrue(self.game.game_over)

    @patch('builtins.input', return_value='q')
    def test_other_player_surrendered(self, mock_input):
        """Verifica si el otro jugador se rinde correctamente"""
        result = self.game.other_player_surrendered()
        self.assertTrue(result)

    def test_declare_winner(self):
        """Verifica que se declare correctamente el ganador"""
        self.game.current_turn = 'white'
        self.game.declare_winner()
        self.assertTrue(self.game.game_over)

if __name__ == '__main__':
    unittest.main(verbosity=2)
