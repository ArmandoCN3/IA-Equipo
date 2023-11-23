import math
import os

class TicTacToe:
    def __init__(self):
        self.board = ['-' for _ in range(16)]
        self.usuario = 'X'
        self.computadora = "O"

    def mostrarTablero(self):
        print("\n  0   1   2   3")
        for i in range(4):
            print(f"{i} {self.board[0 + (i * 4)]} | {self.board[1 + (i * 4)]} | {self.board[2 + (i * 4)]} | {self.board[3 + (i * 4)]}")

    def tableroLleno(self, tablero):
        return not "-" in tablero

    def jugadasGanadoras(self, tablero, jugador):
        # Horizontales
        if tablero[0] == tablero[1] == tablero[2] == tablero[3] == jugador: return True
        if tablero[4] == tablero[5] == tablero[6] == tablero[7] == jugador: return True
        if tablero[8] == tablero[9] == tablero[10] == tablero[11] == jugador: return True
        if tablero[12] == tablero[13] == tablero[14] == tablero[15] == jugador: return True

        # Verticales
        if tablero[0] == tablero[4] == tablero[8] == tablero[12] == jugador: return True
        if tablero[1] == tablero[5] == tablero[9] == tablero[13] == jugador: return True
        if tablero[2] == tablero[6] == tablero[10] == tablero[14] == jugador: return True
        if tablero[3] == tablero[7] == tablero[11] == tablero[15] == jugador: return True

        # Diagonales
        if tablero[0] == tablero[5] == tablero[10] == tablero[15] == jugador: return True
        if tablero[3] == tablero[6] == tablero[9] == tablero[12] == jugador: return True

        return False

    def verificarGanador(self):
        if self.jugadasGanadoras(self.board, self.usuario):
            os.system("cls")
            print(f"\n GANASTE")
            return True

        if self.jugadasGanadoras(self.board, self.computadora):
            os.system("cls")
            print(f"\n PERDISTE")
            return True

        if self.tableroLleno(self.board):
            os.system("cls")
            print("\n EMPATE")
            return True

        return False

    def juegoPrincipal(self):
        pc = Computadora()
        humano = Usuario()
        
        while True:
            os.system("cls")
            print(f"\n----------JUEGO DEL GATO----------\n")
            print(f"\n Turno de X:")
            self.mostrarTablero()

            casilla = humano.tiroUsuario(self.board)
            self.board[casilla] = self.usuario
            if self.verificarGanador():
                break

            casilla = pc.tiroComputadora(self.board)
            self.board[casilla] = self.computadora
            if self.verificarGanador():
                break

        print()
        self.mostrarTablero()

class Usuario:
    def __init__(self):
        self.letra = 'X'

    def tiroUsuario(self, tablero):
        while True:
            try:
                entrada = input(f"Ingrese su posición (fila , columna): ")
                fila, columna = map(int, entrada.split('.'))
                casilla = fila * 4 + columna

                if 0 <= fila <= 3 and 0 <= columna <= 3 and tablero[casilla] == "-":
                    return casilla
                else:
                    print("Posición no válida. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada no válida. Inténtalo de nuevo.")

class Computadora(TicTacToe):
    def __init__(self):
        self.computadora = 'O'
        self.usuario = "X"

    def turnoJugador(self, tablero):
        x = tablero.count("X")
        o = tablero.count("O")
        return "X" if x == o else "O"

    def posicionesVacias(self, tablero):
        return [i for i, x in enumerate(tablero) if x == "-"]

    def resultado(self, tablero, action):
        nuevoTablero = tablero.copy()
        jugador = self.turnoJugador(tablero)
        nuevoTablero[action] = jugador
        return nuevoTablero

    def finJuego(self, tablero):
        if self.jugadasGanadoras(tablero, "X"):
            return True
        if self.jugadasGanadoras(tablero, "O"):
            return True
        return False

    def minimax(self, tablero, jugador, alpha=-math.inf, beta=math.inf, depth=4):
        max_jugador = self.usuario
        min_jugador = 'O' if jugador == 'X' else 'X'

        if self.finJuego(tablero):
            posicionesDisponibles = len(self.posicionesVacias(tablero)) + 1
            
            if min_jugador == max_jugador:
                return {'position': None, 'puntuacion': 1 * posicionesDisponibles}
            else:
                return {'position': None, 'puntuacion': -1 * posicionesDisponibles}
        elif self.tableroLleno(tablero):
            return {'position': None, 'puntuacion': 0}


        if depth == 0:
            return {'position': None, 'puntuacion': self.evaluar(tablero)}

        if jugador == max_jugador:
            mejorMov = {'position': None, 'puntuacion': -math.inf}
            for posibleMov in self.posicionesVacias(tablero):
                nuevoTablero = self.resultado(tablero, posibleMov)
                puntuacionHijo = self.minimax(nuevoTablero, min_jugador, alpha, beta, depth - 1)

                puntuacionHijo['position'] = posibleMov

                if puntuacionHijo['puntuacion'] > mejorMov['puntuacion']:
                    mejorMov = puntuacionHijo

                alpha = max(alpha, mejorMov['puntuacion'])
                if alpha >= beta:
                    break

            return mejorMov
        else:
            mejorMov = {'position': None, 'puntuacion': math.inf}
            for posibleMov in self.posicionesVacias(tablero):
                nuevoTablero = self.resultado(tablero, posibleMov)
                puntuacionHijo = self.minimax(nuevoTablero, min_jugador, alpha, beta, depth - 1)

                puntuacionHijo['position'] = posibleMov

                if puntuacionHijo['puntuacion'] < mejorMov['puntuacion']:
                    mejorMov = puntuacionHijo

                beta = min(beta, mejorMov['puntuacion'])
                if alpha >= beta:
                    break

            return mejorMov

    def evaluar(self, tablero):
        puntuacion = 0
        for i in range(16):
            if tablero[i] == self.computadora:
                puntuacion += 1
            elif tablero[i] == self.usuario:
                puntuacion -= 1
        return puntuacion

    def tiroComputadora(self, tablero):
        casilla = self.minimax(tablero, self.computadora)['position']
        return casilla

if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
    tic_tac_toe.juegoPrincipal()