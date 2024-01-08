# Goruntulerin perspektifini ayarlamayi ogrenecegiz


import cv2
import numpy as np

# içe aktar resim
img = cv2.imread("kart.png")
cv2.imshow("Original", img)

width = 400
height = 500

#pts1 point uzerinden resmiimizi actik koselerindeki index leri buraya yazdik
#pts2 ise olmasi gereken degerleri girdik 1)sol ust>2)sol alt>3)sag ust>4)sag alt koseler
pts1 = np.float32([[203,1],[1,472],[540,150],[338,617]])
pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])

matrix =cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

#nihai donusturulmus resim
imgOutput = cv2.warpPerspective(img, matrix, (width,height))
cv2.imshow("Niahi resim", imgOutput)


