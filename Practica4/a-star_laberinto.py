from queue import PriorityQueue
from randomMaze import *
import time

def distancia (punto1, punto2): #Función Heurística h(n)
    return abs(punto1[0] - punto2[0]) + abs(punto1[1] - punto2[1])

def resolver(laberinto, inicio, fin):
    nodos_frontera = PriorityQueue()
    nodos_visitados = []
    nodos_frontera.put((distancia(inicio,fin), [inicio]))

    while not nodos_frontera.empty():
        _, path = nodos_frontera.get()
        x,y = path[-1]  # Obtener la última posición del camino actual

        if (x,y) == fin:
            return True, path

        nodos_visitados.append((x,y))

        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(laberinto) and 0 <= ny < len(laberinto[0]):
                if laberinto[nx][ny] == '0' and (nx, ny) not in nodos_visitados:
                    nuevo_camino = list(path)
                    nuevo_camino.append((nx, ny))
                    costo = distancia((nx, ny), fin)
                    nodos_frontera.put((costo, nuevo_camino))

    return False, []

if __name__ == "__main__":
    tiempo_inicio = time.time()
    solved, nodos_visitados = resolver(laberinto, inicio, fin)

    if solved:
        print("\nLaberinto Resuelto!\n")
        for x, y in nodos_visitados:
            if laberinto[x][y] != 'S' and laberinto[x][y] != 'E':
                laberinto[x][y] = '*'
        for row in laberinto:
            print("".join(row))
    else:
        print("\nNo se encontró solucion")
    
    tiempo_fin = time.time()
    print(f"Tiempo de ejecución: {tiempo_fin - tiempo_inicio}")   