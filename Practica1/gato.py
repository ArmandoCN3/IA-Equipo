import random

fila1 = ["-","-","-"]
fila2 = ["-","-","-"]
fila3 = ["-","-","-"]
tablero = [fila1, fila2, fila3]
casillas_ocupadas = []

#Función que valida los movimientos del usuario
def usuario():
    print(f"    0    1    2\n0 {fila1}\n1 {fila2}\n2 {fila3}")
    valid = False #Variable que se valida hasta que la casilla ingresada esté disponible o sea válida

    while not valid:
        if len(casillas_ocupadas) == 9:
            break #Rompe el ciclo en caso de que haya 9 posiciones ocupadas
        posicion = input("Donde quieres poner la X?: ")

        if len(posicion) == 3:
            fila = int(posicion[0])
            columna = int(posicion[2])
            casilla = [fila,columna]

            if 0 <= fila <= 2 and 0 <= columna <= 2:
                if casilla not in casillas_ocupadas:
                    valid = True #Validación de casilla disponible y correcta
                    casillas_ocupadas.append(casilla)  # Agregar la casilla a la lista de ocupadas
                    tablero[fila][columna] = "X" #Poner el tiro en el tablero
                else:
                    print("Esa posición ya está ocupada. Inténtalo de nuevo.")
            else:
                print("Los valores deben estar entre 0 y 2. Intentalo de nuevo.")
        else:
            print("La entrada debe tener el formato 'fila,columna'. Intentalo de nuevo.")


# Función que valida los movimientos de la computadora
def computadora(value):
    valid = False #Variable que se valida hasta que la casilla esté disponible
    
    while not valid:
        if len(casillas_ocupadas) == 9:
            break #Rompe el ciclo en caso de que ya no haya espacios en el tablero
        
        fila_pc = random.randint(0, 2) #Genera aleatoriamente la fila y columna entre 0,1,2
        columna_pc = random.randint(0, 2)
        casilla_pc = [fila_pc, columna_pc]

        if casilla_pc not in casillas_ocupadas:  # Verificar si la casilla ya está ocupada
            valid = True
            casillas_ocupadas.append(casilla_pc)  # Agregar la casilla a la lista de ocupadas
            tablero[fila_pc][columna_pc] = value  #Agrega al tablero el parámetro X ó O

def ganador():
    for i in range(3):
        #VERTICALES
        if tablero[0][i] == tablero[1][i] == tablero[2][i]: #Determina si hay alguna combinación ganadora en vertical
            if tablero[0][i] == 'X': #Determina si quien ganó fue X ó O
                print(f"\n HA GANADO 'X'")
                return True
            elif tablero[0][i] == 'O':
                print(f"\n HA GANADO 'O'")
                return True
            
        #HORIZONTALES
        if tablero[i][0] == tablero[i][1] == tablero[i][2]: #Determina si hay alguna combinación ganadora en horizontal
            if tablero[i][0] == 'X': #Determina si quien ganó fue X ó O
                print(f"\n HA GANADO 'X'")
                return True
            elif tablero[i][0] == 'O':
                print(f"\n HA GANADO 'O'")
                return True
    #DIAGONALES
    if tablero[0][0] == tablero[1][1] == tablero[2][2]  or tablero[0][2] == tablero[1][1] == tablero[2][0]: #Determina si hay alguna combinación ganadora en diagonal
        if (tablero[1][1] == 'X'): #Determina si quien ganó fue X ó O
            print(f"\n HA GANADO 'X'")
            return True
        elif tablero[0][i] == 'O':
            print(f"\n HA GANADO 'O'")
            return True
    return False

#PROGRAMA PRINCIPAL
contador = 0
print(f"\n----------JUEGO DEL GATO----------\n")
opcion = int(input("Ingrese 1 para Usuario vs Computadora\nIngrese 2 para Computadora vs Computadora: "))

while contador!=9: #Bucle que evita que haya más de 9 tiros
    if opcion == 1: #Juego usuario vs computadora
        usuario()
        if ganador():
            break
        computadora(value="O")
        if ganador():
            break
    elif opcion == 2: #Juego computadora vs computadora
        computadora(value="X")
        print(f"    0    1    2\n0 {fila1}\n1 {fila2}\n2 {fila3}")
        if ganador():
            break
        computadora(value="O")
        print(f"    0    1    2\n0 {fila1}\n1 {fila2}\n2 {fila3}")
        if ganador():
            break

    contador += 1

if contador == 9: #Si hubo 9 tiros y no hubo ganador, hay empate
    print(f"\n EMPATE")

print(f"\nFIN DE LA PARTIDA")
print(f"    0    1    2\n0 {fila1}\n1 {fila2}\n2 {fila3}")