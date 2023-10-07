import random

def position(x, y):
    return '1' if random.randint(1, 4) == 1 else '0' 

size = int(input("\nIngrese el tamano del laberinto (NxN): "))

laberinto = [[position(x, y) for y in range(size)] for x in range(size)]

inicio = (0, 0)
fin = (size - 2, size - 2)
laberinto[inicio[0]][inicio[1]] = 'S'
laberinto[fin[0]][fin[1]] = 'E'

for row in laberinto:
    print("".join(row))

laberinto[inicio[0]][inicio[1]] = '0'
laberinto[fin[0]][fin[1]] = '0'
