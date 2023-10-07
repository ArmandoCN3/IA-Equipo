import random
import math

# Función que calcula el costo
def costo(x):
    # f(x) = x^4 + 3x^3 + 2x^2 - 1
    return x**4 + 3*x**3 + 2*x**2 - 1

    # f(f) = x^2 - 3x - 8
    #return x**2 -3*x - 8

# Parámetros del algoritmo de recocido simulado
temperatura_inicial = 1000.0
temperatura_minima = 0.1
factor_enfriamiento = 0.95
iteraciones_por_temperatura = 100

# Valor inicial aleatorio para x
x_actual = random.uniform(-10, 10)
mejor_x = x_actual
mejor_costo = costo(x_actual)

# Bucle principal del recocido simulado
temperatura = temperatura_inicial
while temperatura > temperatura_minima:
    for _ in range(iteraciones_por_temperatura):
        # Generar una solución vecina aleatoria
        x_vecino = x_actual + random.uniform(-0.1, 0.1)
        costo_vecino = costo(x_vecino)
        
        delta_costo = costo_vecino - mejor_costo
        
        if delta_costo < 0 or random.random() < math.exp(-delta_costo / temperatura):
            x_actual = x_vecino
            mejor_costo = costo_vecino
            
            
            if costo_vecino < costo(mejor_x):
                mejor_x = x_vecino
    
    # Enfriar la temperatura
    temperatura *= factor_enfriamiento

print("Mejor solución encontrada: x =", mejor_x)
print("Valor mínimo de la función:", costo(mejor_x))