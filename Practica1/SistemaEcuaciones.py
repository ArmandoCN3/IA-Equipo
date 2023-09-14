import random
import os
import numpy as np
"""
    Este programa resuelve por numeros aleatorios
    el siguiente sistema de ecuaciones (rango -100 a 100)
    16B- 6D + 4E + F = -36
    B  - 8D + E  + F = -64
    16B+ 2D - 4E + F = -4
    9B + 8D - 3E + F = -64
"""
x = 0
espe1 = []
espe2 = []
espe3 = []
espe4 = []

while(x != 100):
    os.system("cls")
    B= random.randint(-100,100)
    D= random.randint(-100,100)
    E= random.randint(-100,100)
    F= random.randint(-100,100)
    r = random.randint(-100,100)
    
    print("Valores probados: ")
    print("B:",B)
    print("D:",D)
    print("E:",E)
    print("F:",F)

    ecu1 = 16*B- 6*D + 4*E + F
    ecu2 = B  - 8*D + E  + F
    ecu3 = 16*B+ 2*D - 4*E + F
    ecu4 = 9*B + 8*D - 3*E + F
    
    print("Resultados de las ecuaciones")
    print("ecu1:",ecu1)
    print("ecu2:",ecu2)
    print("ecu3:",ecu3)
    print("ecu4:",ecu4)
    
    x1 = -36-ecu1
    x2 = -64-ecu2
    x3 = -4 -ecu3
    x4 = -64-ecu4   
    if(x1 < 0):
        x1=x1*-1
    if(x2 < 0):
        x2=x2*-1
    if(x3 < 0):
        x3=x3*-1
    if(x4 < 0):
        x4=x4*-1    
        
    espe1.append(x1)
    espe2.append(x2)
    espe3.append(x3)
    espe4.append(x4)
    

    if((ecu1 == -36) &  (ecu2 == -64) & (ecu3 == -4) & (ecu4 == -64)):
        print("El sistema se resolvió con los valores: ")
        print(B)
        print(D)
        print(E)
        print(F)
        x=100
    x+=1
    
min1 = np.amin(espe1)
min2 = np.amin(espe2)
min3 = np.amin(espe3)
min4 = np.amin(espe4)
    
print("El programa estuvo a", min1, "de acertar la 1ra ecuacion")
print("El programa estuvo a", min2, "de acertar la 2da ecuacion")
print("El programa estuvo a", min3, "de acertar la 3ra ecuacion")
print("El programa estuvo a", min4, "de acertar la 4ta ecuacion")
