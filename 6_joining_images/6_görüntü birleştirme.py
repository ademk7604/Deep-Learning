# Birden fazla goruntunun birlestirilmesini ogrenecegiz
import cv2
import numpy as np

#resmi ice aktar
img = cv2.imread("lenna.png")
cv2.imshow("Original", img)

#yatay
hor = np.hstack((img,img))
cv2.imshow("Horizontal", hor)

# nesne takibi tespiti algoritmamziii olustururken kullaniriz
#dikey
ver = np.vstack((img,img))
cv2.imshow("Vertical", ver)

