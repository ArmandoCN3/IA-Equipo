import time

def resolver_laberinto(laberinto, inicio, fin):
    pila = [inicio] #Pila que recibe las coordenadas de inicio
    while pila: #Mientras la pila tenga valores
        x, y = pila[-1] #Coordenadas del último elemento en la pila, posición actual del algoritmo

        if (x, y) == fin: #Si llegó al punto de llegada o fin
            return True, pila #Sale  del bucle y retorna la pila con el camino

        laberinto[x][y] = '2' #Marca la posición como visitada y coloca un 2 en la matriz laberinto

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: #Itera sobre las cuatro posibles direcciones: →, ↓, ← y ↑.
            nx, ny = x + dx, y + dy #Calcula las nuevas coordenadas

            if 0 <= nx < len(laberinto) and 0 <= ny < len(laberinto[0]): #Verifica si las nuevas coordenadas están dentro de los límites del laberinto
                if laberinto[nx][ny] == '0' or laberinto[nx][ny] == 'E': #Comprueba si la nueva posición es un camino abierto o el punto final
                    pila.append((nx, ny)) #Agrega las nuevas coordenadas a la pila y rompe el bucle 
                    break
        else:
            pila.pop() #Si no se puede mover en ninguna direccion, retrocede desapilando la última posición.
    
    return False, [] #Si la pila está vacía y no se ha encontrado una solución, la función retorna False y una lista vacía.


if __name__ == "__main__":
    # 0 = camino abierto, 1 = pared, S = inicio, E = fin
    laberinto = [ #Laberinto con solución:
    ['1', '1', '1', '1'],
    ['S', '0', '0', '1'],
    ['1', '0', '1', '0'],
    ['1', '0', '0', 'E']
    ]
    inicio = (1, 0)
    fin = (3, 3)

    tiempo_inicio = time.time()
    resuelto, camino = resolver_laberinto(laberinto, inicio, fin) 
    #Llama a la función y devuelve True/False para resuelto y para el camino la lista con el camino o lista vacía

    if resuelto: #Si está resuelto, pone un * en las posiciones de la lista "camino"
        print("\nLaberinto resuelto!")
        for x, y in camino:
            if laberinto[x][y] != 'S' and laberinto[x][y] != 'E': #Pone asteristo excepto en S y E
                laberinto[x][y] = '*'
        for fila in laberinto:
            print("".join(fila))
    else:
        print("No se encontró solución") #No se encontró solución y no hay camino

    tiempo_fin = time.time()
    print("Tiempo de ejecución: ")
    print(tiempo_fin - tiempo_inicio)

