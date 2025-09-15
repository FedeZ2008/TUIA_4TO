import numpy as np
from matplotlib import pyplot as plt
import cv2



x = np.array([1,2,4])
print(x)
print("hola")

plt.figure(), plt.plot(x), plt.title('Ejemplo 1'), plt.show()

img = cv2.imread('xray-chest.png',cv2.IMREAD_GRAYSCALE)
plt.figure(), plt.imshow(img, cmap='gray'), plt.title('Ejemplo 2'), plt.show()
