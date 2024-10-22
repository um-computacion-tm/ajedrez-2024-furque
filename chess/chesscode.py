from chess.pieces import King,Knight,Rook,Bishop,Pawn,Queen
from chess.board import Board
from chess.user import user

class Chess:
    def __init__(self):
        # Inicializa el tablero, jugador y estado del juego
        self.board = Board()
        self.player = user(self.board)
        self.current_turn = 'white'  # El turno comienza con las piezas blancas
        self.game_over = False  # Controla si el juego ha terminado
        
    # Controla el flujo del turno actual del jugador
    def play_turn(self):
        if self.game_over:
            return False  
        self.board.print_board()  # Imprime el estado actual del tablero
        print(f"Le toca a {self.current_turn}")
        origin = self.get_user_input("Escoge la posicion de inicio o oprime 'q' para rendirte: ")
        if origin.lower() == 'q':  # Si el jugador se rinde
            self.handle_surrender()
            return False  

        # Solicita la posición de destino de la pieza
        destination = self.get_user_input("Escoge la posicion de destino de la pieza: ")
        try:
            # Convierte la notación en coordenadas del tablero
            x1, y1, x2, y2 = self.get_positions_from_notation(origin, destination)
            print()
            self.attempt_move(x1, y1, x2, y2) 
        except (ValueError, IndexError):
            print("Posicion Invalida. Inténtalo de nuevo.")  # Captura errores de formato

        return True  # El juego sigue

    def get_user_input(self, prompt):
        return input(prompt)  

    # Convierte notaciones en coordenadas
    def get_positions_from_notation(self, origin, destination):
        x1, y1 = self.board.get_position_from_notation(origin)
        x2, y2 = self.board.get_position_from_notation(destination)
        return x1, y1, x2, y2

    # Intenta mover la pieza desde una posición inicial a una nueva posición
    def attempt_move(self, x1, y1, x2, y2):
        piece = self.board.get_piece_at(x1, y1)  
        if self.is_valid_piece(piece):  
            self.execute_move(piece, x2, y2)  
        else:
            print("Revisa tu movimiento o turno.")

    # Verifica si la pieza pertenece al jugador en turno
    def is_valid_piece(self, piece):
        return piece and piece.get_color() == self.current_turn

    def execute_move(self, piece, x2, y2):
        if piece.is_valid_move(x2, y2, self.board) and self.board.move_piece(piece, x2, y2):
            self.check_winner()  # Verifica si el juego ha terminado


    def handle_surrender(self):
        print(f"El jugador {self.current_turn} ha decidido rendirse.")
        if self.other_player_surrendered():
            print("El juego termina en empate debido a un acuerdo entre los jugadores")
        else:
            print(f"El jugador {self.current_turn} es el perdedor.")
        self.game_over = True  # El juego termina

    # Verifica si el oponente también se rinde
    def other_player_surrendered(self):
        return self.get_user_input(f"El jugador oponente debe presionar 'q' para rendirse: ").lower() == 'q'

    # Verifica si el juego tiene un ganador tras el turno
    def check_winner(self):
        self.switch_turn()  #
        if not self.player.has_pieces(self.current_turn) or not self.player.has_king(self.current_turn):
            self.declare_winner()  # Si no quedan piezas o el rey fue capturado, se declara un ganador

    # Alterna el turno entre los jugadores
    def switch_turn(self):
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'

    # Declara el ganador del juego
    def declare_winner(self):
        winner = 'black' if self.current_turn == 'white' else 'white'
        print(f"El jugador {winner} es el gandor!!.")
        self.game_over = True  # El juego termina
