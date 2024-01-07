import cv2
import numpy as np
import os
import csv
from keras.utils import to_categorical
import mahotas


# Parámetros
direccion = '/content/drive/MyDrive/shapes2'
os.chdir(direccion)
tamano_img = 60

def aplanar(dimDatos, imagenes):
    imagenes = np.array(imagenes)
    imagenes = imagenes.reshape(len(imagenes), dimDatos)
    imagenes = imagenes.astype('float32')
    imagenes /= 255
    return imagenes

def calcula_momentos_hu(imagen):
    momentos = cv2.moments(imagen)
    momentos_hu = cv2.HuMoments(momentos)
    # Transformar a logaritmo para hacerlos invariantes a escala
    return -np.sign(momentos_hu) * np.log10(np.abs(momentos_hu))

def calcular_momentos_zernike(imagen, radio, grado):
    momentos_zernike = mahotas.features.zernike_moments(imagen, radio, grado)
    return momentos_zernike

# Obtener datos
carpetas, etiquetas, imagenes = ['triangle', 'star', 'square', 'circle'], [], []
for carpeta in carpetas:
    print(carpeta)
    for path in os.listdir(os.getcwd()+'/'+carpeta):
        img = cv2.imread(carpeta+'/'+path, 0)
        imagenes.append(cv2.resize(img, (tamano_img, tamano_img)))
        etiquetas.append(carpeta)
        
# Calcular momentos de Hu y Zernike para cada imagen
momentos_hu = np.array([calcula_momentos_hu(imagen) for imagen in imagenes])
momentos_zernike = np.array([calcular_momentos_zernike(imagen, 21, 8) for imagen in imagenes])

import csv

# Guardar los resultados en archivos CSV - Hu Moments
with open('P2_hu_moments.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Escribir el encabezado
    header = ["Hu Moment " + str(i) for i in range(momentos_hu.shape[1])]
    header += ["Actual Label"]
    writer.writerow(header)

    # Escribir los datos
    for i in range(len(momentos_hu)):
        row = np.concatenate([momentos_hu[i], [etiquetas[i]]], axis=None)  # Asegura que ambos arrays sean 1D
        writer.writerow(row)

print("Resultados de Hu guardados en archivo CSV.")

# Guardar los resultados en archivos CSV - Zernike Moments
with open('P2_zernike_moments.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Escribir el encabezado
    header_zernike = ["Zernike Moment " + str(i) for i in range(momentos_zernike.shape[1])]
    header_zernike += ["Actual Label"]
    writer.writerow(header_zernike)

    # Escribir los datos
    for i in range(len(momentos_zernike)):
        row = np.concatenate([momentos_zernike[i], [etiquetas[i]]])
        writer.writerow(row)

print("Resultados de Zernike guardados en archivo CSV.")


