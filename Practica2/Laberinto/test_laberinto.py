laberinto = [ #Laberinto con solución:
    ['1', '1', '1', '1'],
    ['S', '0', '0', '1'],
    ['1', '0', '1', '0'],
    ['1', '0', '0', 'E']
]
inicio = (1, 0)
fin1 = (3, 3)

laberinto = [ #Laberinto sin solución (punto final bloqueado)
    ['1', '1', '1', '1', '1'],
    ['S', '0', '1', '1', '1'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', 'E']
]
inicio = (1, 0)
fin = (4, 4)

laberinto = [ #Laberinto sin solución (punto de inicio bloqueado)
    ['S', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1'],
    ['1', '0', '1', '1', '1'],
    ['1', '0', '1', '1', 'E'],
    ['1', '1', '1', '1', '1']
]
inicio = (0, 0)
fin = (3, 4)

laberinto = [ #Laberinto con solución
    ['1', '1', '1', '1', '1'],
    ['S', '0', '0', '0', '1'],
    ['1', '1', '1', '0', '1'],
    ['1', '0', '0', '0', 'E'],
    ['1', '1', '1', '1', '1']
]
inicio = (1, 0)
fin = (3, 4)

laberinto = [ #Laberinto sin solución (no hay camino al punto final)
    ['1', '1', '1', '1', '1'],
    ['S', '0', '1', '1', '1'],
    ['1', '1', '1', '0', '1'],
    ['1', '1', '1', '0', 'E'],
    ['1', '1', '1', '1', '1']
]
inicio = (1, 0)
fin = (3, 4)

laberinto = [#Laberinto con solución
    ['1', '1', '1', '1', '1'],
    ['S', '0', '1', '1', '1'],
    ['1', '0', '1', '0', '1'],
    ['1', '0', '0', '0', 'E'],
    ['1', '1', '1', '1', '1']
]
inicio = (1, 0)
fin6 = (3, 4)

laberinto = [ #Laberinto sin solución (punto final inaccesible)
    ['1', '1', '1', '1', '1'],
    ['S', '0', '1', '1', '1'],
    ['1', '1', '0', '0', '1'],
    ['1', '1', '1', '1', 'E'],
    ['1', '1', '1', '1', '1']
]
inicio = (1, 0)
fin7 = (3, 4)

laberinto = [ #Laberinto con solución
    ['1', '1', '1', '1', '1'],
    ['S', '0', '0', '0', '1'],
    ['1', '1', '1', '0', '1'],
    ['1', '0', '0', '0', 'E'],
    ['1', '1', '1', '1', '1']
]
inicio = (1, 0)
fin = (3, 4)

laberinto = [ #Laberinto sin solución (punto de inicio inaccesible)
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '1'],
    ['1', '0', '0', '0', '1'],
    ['1', '1', '1', '1', 'E'],
    ['1', '1', '1', '1', '1']
]
inicio = (0, 1)
fin = (3, 4)

laberinto = [#Laberinto con solución 10x10
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['S', '0', '0', '1', '1', '1', '0', '0', '0', '1'],
    ['1', '1', '0', '0', '0', '0', '0', '1', '0', '1'],
    ['1', '1', '1', '1', '0', '1', '0', '1', '0', '1'],
    ['1', '0', '0', '0', '0', '1', '0', '1', '0', '1'],
    ['1', '0', '1', '1', '1', '1', '0', '1', '0', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', 'E', '1']
]
inicio = (1, 0)
fin = (9, 8)

laberinto = [ #Laberinto con solución 20x50
    # 0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47   48   49
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['S', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0'],
    ['1', '1', '0', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '1', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '1', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0'],
    ['1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '1', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '1', '1', '0', '0', '0', '0'],
    ['1', '0', '0', '1', '0', '1', '1', '1', '1', '0', '1', '1', '1', '1', '0', '1', '1', '0', '0', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0'],
    ['1', '0', '0', '1', '0', '1', '0', '0', '1', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '1', '1', '0', '1', '0', '0', '1', '1', '0', '0', '0', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '0', '1', '0', '0'],
    ['1', '0', '0', '1', '0', '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '0', '1', '1', '0', '1', '1', '0', '1', '1', '0', '1', '0', '1', '0', '0', '1', '0', '0'],
    ['1', '0', '0', '1', '0', '1', '1', '1', '1', '0', '1', '0', '0', '0', '1', '1', '1', '0', '1', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '1', '0'],
    ['1', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1', '0', '0'],
    ['1', '0', '0', '1', '0', '1', '1', '1', '1', '1', '1', '0', '1', '1', '0', '0', '1', '1', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0'],
    ['1', '0', '0', '1', '0', '1', '0', '0', '0', '0', '1', '0', '1', '0', '0', '1', '0', '1', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '0', '0', '0', '1', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '0', '1', '1', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '0', '0', '1', '1', '1', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '0', '1', '0', '1', '0', '0', '1'],
    ['1', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0', '0', '1', '0', '1', '1', '1', '0', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '1', '1', '1', '0', '1', '1', '1', '1', '0', '1', '0', '0', '0', '0', '1'],
    ['1', '0', '0', '1', '0', '1', '1', '1', '1', '0', '1', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1', '0', '0', '1', '1', '0', '0', '1', '0', '0', '0', '0', '1', '0', '1', '1', '1', '0', '1', '1', '1', '0', '0', '0', '1', '0', '0'],
    ['1', '1', '0', '0', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1', '0', '1', '0', '1', '1', '0', '1', '1', '0', '1', '0', '0', '0', '1', '1', '1', '0', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '0', '1', '0', '1'],
    ['0', '0', '1', '0', '1', '1', '1', '0', '0', '1', '0', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '1', '0', '1', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '1', '0', '0', '1'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1', '1', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '1', '0', '1', '0', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', 'E', '1']
]
inicio = (1, 0)
fin = (20, 48)

laberinto = [ #Laberinto con recorrido en todas las casillas
    ['E', '0', '0', '0'],
    ['0', '0', '0', '0'],
    ['0', '0', '0', '0'],
    ['0', '0', '0', 'S'],
]

inicio = (3, 3)
fin = (0, 0)

laberinto = [ #Laberinto con solo dos caminos posibles
    ['S', '0', '0', '0'],
    ['0', '1', '1', '0'],
    ['0', '1', '1', '0'],
    ['0', '0', '0', 'E']
]

inicio = (0, 0)
fin = (3, 3)
