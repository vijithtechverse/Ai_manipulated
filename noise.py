import cv2
import numpy as np

def noise_analysis(image):
    img = np.array(image.convert("L"))
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    variance = laplacian.var()
    return variance
