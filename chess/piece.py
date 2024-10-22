class Piece:
    def __init__(self, x, y, color):
        # Inicializa la posición (x, y) y el color de la pieza
        self.__x__ = x
        self.__y__ = y
        self.__color__ = color

    def get_position(self):
        return self.__x__, self.__y__

    
    def set_position(self, x, y):
        self.__x__ = x
        self.__y__ = y

    
    def get_color(self):
        return self.__color__

    # Retorna el ícono correspondiente al color de la pieza
    def get_icon(self):
        return self.white_icon if self.__color__ == 'white' else self.black_icon

    
    def is_same_color_piece(self, new_x, new_y, board):
        target_piece = board.get_piece_at(new_x, new_y)
        return target_piece and target_piece.get_color() == self.__color__

    # Debe ser implementado por las subclases para validar movimientos específicos
    def is_valid_move(self, new_x, new_y, board):
        raise NotImplementedError("Este método debe ser definido en las subclases específicas")

    # Verifica si el camino hacia la nueva posición está despejado
    def is_path_clear(self, new_x, new_y, board):
        if new_x == self.__x__:  # Movimiento vertical
            return self.is_vertical_path_clear(new_y, board)
        elif new_y == self.__y__:  # Movimiento horizontal
            return self.is_horizontal_path_clear(new_x, board)
        return self.is_diagonal_path_clear(new_x, new_y, board)  # Movimiento diagonal

    # Comprueba si el movimiento es posible
    def check_move(self, new_x, new_y, board):
        return self.is_path_clear(new_x, new_y, board) and not self.is_same_color_piece(new_x, new_y, board)

    # Valida el movimiento dependiendo del tipo (recto o diagonal) y el camino despejado
    def is_valid_move_type(self, new_x, new_y, board, move_type_check):
        return move_type_check(new_x, new_y) and self.check_move(new_x, new_y, board)

    # Valida los movimientos en línea recta
    def is_valid_straight_move(self, new_x, new_y, board):
        return self.is_valid_move_type(new_x, new_y, board, self.is_straight_move)

    # Valida los movimientos en diagonal
    def is_valid_diagonal_move(self, new_x, new_y, board):
        return self.is_valid_move_type(new_x, new_y, board, self.is_diagonal_move)

    # Verifica si no hay piezas en el camino horizontal hacia el nuevo x
    def is_horizontal_path_clear(self, new_x, board):
        step = 1 if new_x > self.__x__ else -1
        return all(board.get_piece_at(x, self.__y__) is None for x in range(self.__x__ + step, new_x, step))

    # Verifica si no hay piezas en el camino vertical hacia el nuevo y
    def is_vertical_path_clear(self, new_y, board):
        step = 1 if new_y > self.__y__ else -1
        # Recorre todas las posiciones entre el origen y destino, asegurándose de que estén vacías
        return all(board.get_piece_at(self.__x__, y) is None for y in range(self.__y__ + step, new_y, step))

    # Verifica si no hay piezas en el camino diagonal hacia la nueva posición
    def is_diagonal_path_clear(self, new_x, new_y, board):
        dx = 1 if new_x > self.__x__ else -1
        dy = 1 if new_y > self.__y__ else -1
        x, y = self.__x__ + dx, self.__y__ + dy
        while x != new_x and y != new_y:
            if board.get_piece_at(x, y):
                return False
            x += dx
            y += dy
        return True

    # Verifica si el movimiento es en línea recta (horizontal o vertical)
    def is_straight_move(self, new_x, new_y):
        return new_x == self.__x__ or new_y == self.__y__

    # Verifica si el movimiento es diagonal
    def is_diagonal_move(self, new_x, new_y):
        return abs(new_x - self.__x__) == abs(new_y - self.__y__) and new_x != self.__x__ and new_y != self.__y__

