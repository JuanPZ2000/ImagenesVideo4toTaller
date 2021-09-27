# This is a sample Python script.
from Quadrilateral import Quadrilateral
import cv2
import Corners as Cn
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
if __name__ == '__main__':
    xd = Quadrilateral(500)

    xd2 = xd.generate()
    cv2.imshow("uwu",xd2)
    high_thresh = 300
    bw_edges = cv2.Canny(xd2, high_thresh*0.3, high_thresh, L2gradient=True)
    Cn.DetectCorners(xd2, bw_edges)
    cv2.waitKey(0)