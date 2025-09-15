import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('img_calculadora.tif',cv2.IMREAD_GRAYSCALE)
img.shape
plt.figure()
plt.imshow(img, cmap='gray')
plt.show(block=True)