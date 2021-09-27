from hough import Hough
import cv2
import numpy as np

def DetectCorners(image, bw_edges):
    # high_thresh = 300
    # bw_edges = cv2.Canny(image, 100, 200, L2gradient=True)
    hough = Hough(bw_edges)
    accumulator = hough.standard_transform()

    acc_thresh = 50
    N_peaks = 10
    nhood = [100, 100]
    peaks = hough.find_peaks(accumulator, nhood, acc_thresh, N_peaks)
    _, cols = image.shape[:2]
    image_draw = np.copy(image)
    pendiente = []
    corte = []


    for peak in peaks:
        rho = peak[0]
        theta_ = hough.theta[peak[1]]
        theta_pi = np.pi * theta_ / 180
        theta_ = theta_ - 180

        pendiente.append(-1 / np.tan(theta_pi))
        corte.append((rho * np.sin(theta_pi))-(pendiente[-1] * rho * np.cos(theta_pi)))

        a = np.cos(theta_pi)
        b = np.sin(theta_pi)
        x0 = a * rho + hough.center_x
        y0 = b * rho + hough.center_y
        c = -rho
        x1 = int(round(x0 + cols * (-b)))
        y1 = int(round(y0 + cols * a))
        x2 = int(round(x0 - cols * (-b)))
        y2 = int(round(y0 - cols * a))
        if np.abs(theta_) < 80:
            image_draw = cv2.line(image_draw, (x1, y1), (x2, y2), [0, 0, 0], thickness=2)
        elif np.abs(theta_) > 100:
            image_draw = cv2.line(image_draw, (x1, y1), (x2, y2), [0, 0, 0], thickness=2)
        else:
            if theta_ > 0:
                image_draw = cv2.line(image_draw, (x1, y1), (x2, y2), [0, 0, 0], thickness=2)
            else:
                image_draw = cv2.line(image_draw, (x1, y1), (x2, y2), [0, 0, 0], thickness=2)

    valorMedio_ = -cols/2
    valorMedio  = cols/2

    for m in range(len(pendiente)):
        for n in range(m+1,len(pendiente)):
            if pendiente[m] != pendiente[n]:
                x = (corte[n] - corte[m]) / (pendiente[m] - pendiente[n])
                y = (pendiente[m] * x) + corte[m]
                if (valorMedio_ <= x <= valorMedio) and (valorMedio_ <= y <= valorMedio):
                    x_vertice = np.int_(x+valorMedio)
                    y_vertice = np.int_(y+valorMedio)
                    cv2.circle(image_draw, (x_vertice,y_vertice), 10, (255,0,0), 2)

    cv2.imshow("frame", bw_edges)
    cv2.imshow("lines", image_draw)
    cv2.waitKey(0)
    a = 1