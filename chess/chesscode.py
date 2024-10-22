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
            return False  # Terminar el juego si ya ha finalizado

        self.board.print_board()  # Imprime el estado actual del tablero
        print(f"Le toca a {self.current_turn}")

        # Solicita la posición inicial de la pieza o la rendición
        origin = self.get_user_input("Escoge la posicion de inicio o oprime 'q' para rendirte: ")
        if origin.lower() == 'q':  # Si el jugador se rinde
            self.handle_surrender()
            return False  # Fin del juego

        # Solicita la posición de destino de la pieza
        destination = self.get_user_input("Escoge la posicion de destino de la pieza: ")
        try:
            # Convierte la notación en coordenadas del tablero
            x1, y1, x2, y2 = self.get_positions_from_notation(origin, destination)
            self.attempt_move(x1, y1, x2, y2)  # Intenta realizar el movimiento
        except (ValueError, IndexError):
            print("Posicion Invalida. Inténtalo de nuevo.")  # Captura errores de formato

        return True  # El juego continúa

    def get_user_input(self, prompt):
        return input(prompt)  # Solicita entrada del usuario

    # Convierte notaciones como 'D2' en coordenadas de matriz
    def get_positions_from_notation(self, origin, destination):
        x1, y1 = self.board.get_position_from_notation(origin)
        x2, y2 = self.board.get_position_from_notation(destination)
        return x1, y1, x2, y2

    # Intenta mover la pieza desde una posición inicial a una nueva posición
    def attempt_move(self, x1, y1, x2, y2):
        piece = self.board.get_piece_at(x1, y1)  # Obtiene la pieza en la posición inicial
        if self.is_valid_piece(piece):  # Verifica si es una pieza válida y si es el turno correcto
            self.execute_move(piece, x2, y2)  # Si es válido, ejecuta el movimiento
        else:
            print("Revisa tu movimiento o turno.")

    # Verifica si la pieza pertenece al jugador en turno
    def is_valid_piece(self, piece):
        return piece and piece.get_color() == self.current_turn

    # Ejecuta el movimiento de la pieza si es válido
    def execute_move(self, piece, x2, y2):
        if piece.is_valid_move(x2, y2, self.board) and self.board.move_piece(piece, x2, y2):
            self.check_pawn_promotion(piece, x2, y2)  # Verifica si hay promoción de peón
            self.check_winner()  # Verifica si el juego ha terminado

    # Verifica si un peón ha alcanzado la promoción y permite elegir una nueva pieza
    def check_pawn_promotion(self, piece, x2, y2):
        if isinstance(piece, Pawn) and piece.is_promotion_move(y2):
            self.promote_pawn(piece, x2, y2)

    # Gestiona la promoción del peón
    def promote_pawn(self, pawn, new_x, new_y):
        options = {"1": Queen, "2": Rook, "3": Bishop, "4": Knight}
        print("Elige la pieza a la que quieres promover tu peón:")
        print("1. Reina\n2. Torre\n3. Alfil\n4. Caballo")
        choice = input("Opción (1-4): ")
        # Si la elección es válida, se promueve el peón a la pieza seleccionada
        new_piece = options.get(choice, Queen)(new_x, new_y, pawn.get_color())
        self.board.promote_pawn(pawn, new_x, new_y, new_piece)

    # Maneja el escenario donde un jugador se rinde
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
        self.switch_turn()  # Cambia el turno al jugador contrario
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
