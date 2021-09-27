# Quadrilateral
# Juan Pablo Zuluaga C 2021 PUJ Procesamiento de imagenes y video

import cv2
import os
import numpy as np
from scipy.stats import uniform as uni

class Quadrilateral:

    def __init__(self, N):
        assert N % 2 == 0, "El numero ingresado es impar, por favor ingrese uno par"
        self.N = N

    def generate(self):
        imagen = np.zeros((self.N, self.N, 3), np.uint8)
        imagen[:, :, :] = [255, 255, 0]

        # Distribucion uniforme
        valorMedio = self.N / 2 - 1

        # Puntos en x

        # Puntos para el primer y tercer cuadrante
        x1 = np.int_(uni.rvs(loc=0, scale=valorMedio, size=2))
        # Punto para el segundo y cuarto cuadrante
        x2 = np.int_(uni.rvs(loc=0, scale=valorMedio, size=2)+self.N/2)

        # Puntos en y
        # Puntos para el primer y segundo cuadrante
        y1 = np.int_(uni.rvs(loc=0, scale=valorMedio, size=2))
        # Punto para el tercer y cuarto cuadrante
        y2 = np.int_(uni.rvs(loc=0, scale=valorMedio, size=2)+self.N/2)

        # Genera el cuadrilatero
        cv2.line(imagen, tuple((x1[0], y1[0])), tuple((x2[0], y1[1])), (255, 0, 255), 5)
        cv2.line(imagen, tuple((x2[0], y1[1])), tuple((x2[1], y2[1])), (255, 0, 255), 5)
        cv2.line(imagen, tuple((x1[1], y2[0])), tuple((x2[1], y2[1])), (255, 0, 255), 5)
        cv2.line(imagen, tuple((x1[1], y2[0])), tuple((x1[0], y1[0])), (255, 0, 255), 5)
        return imagen