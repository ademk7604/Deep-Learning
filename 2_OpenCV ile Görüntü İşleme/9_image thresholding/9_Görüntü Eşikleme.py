# Esik degerlerinin resimler uzerindeki etkisini ogrenecegiz
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img1.jpg")
#matplotlib default olarak renkler biraz karik veriyor o nun icin cmap duzeltiyoruz
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off") # eksenleri kapattik
plt.show()


# esikleme
# threshold bize iki sey return ediyor ilkini almadigimiz icin _, bu sekilde dedik. 60 ile 255 alanlari beyaz yap
# THRESH_BINARY thresh(esik degeriyani genlikleri) ile maxval arasindaki alani siliyor yani beyaz yapacak. 
#Ama THRESH_BINARY kullansaydim tam tersi olur
_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thresh_img, cmap = "gray")
plt.axis("off")
plt.show()

# uyarlamali esik degeri
# ADAPTIVE_THRESH_MEAN_C, uyarlanabilecek algoritma icin kullanilac yontemdir. 8 C e denk gelmektedir
#11, bizim block size miz. pixel icin bir esik degeri hesaplamak icin kullaniliyor
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
plt.figure()
plt.imshow(thresh_img2, cmap = "gray")
plt.axis("off")
plt.show()


























