from chess.chesscode import Chess

def main():
    game = Chess()  # Crea una instancia del juego de ajedrez
    while not game.game_over:  # Mientras el juego no haya terminado
        game.play_turn()  # Llama al método para que el jugador realice su turno

if __name__ == "__main__":
    main()  # Ejecuta la función main al ejecutar el script
