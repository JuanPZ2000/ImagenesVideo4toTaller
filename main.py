# This is a sample Python script.
from Quadrilateral import Quadrilateral
import cv2
import Corners as Cn
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
if __name__ == '__main__':
    quadrilateral = Quadrilateral(500)
    imagen = quadrilateral.generate()
    cv2.imshow("imagen generada",imagen)
    high_thresh = 300
    bw_edges = cv2.Canny(imagen, high_thresh*0.3, high_thresh, L2gradient=True)
    imagenFinal, coordenadas =Cn.DetectCorners(imagen, bw_edges)
    print("Las coordenadas de los bordes encontrados fueron x,y:",coordenadas)
    cv2.imshow('Imagen con bordes', imagenFinal)
    cv2.waitKey(0)