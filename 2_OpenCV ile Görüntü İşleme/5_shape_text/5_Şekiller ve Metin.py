"""
- Sekillerin ornegin cizgi, daire, dikdortgen gibi resim uzerine nasil eklendigini ogrenecegiz.
- Metinlerin resim uzerinde nasil eklendigini ogrenecegiz
"""

import cv2
import numpy as np

#resim olustur
img = np.zeros((512,512,3), np.uint8) # siyah bir resime karsilik geliyor 3
print(img.shape)

cv2.imshow("Siyah: ", img)

# cizgi 
# R red G green B blue, RGB = (0 kirmizi, 250 yesil, 0 mavi)
# (resim, baslangic noktasi, bitis noktasi, renk, kalinlik)
cv2.line(img, (0,0),        (512,512),   (0,255,0), 3) 
cv2.imshow("Cizgi: ", img)

# dikdortgen rectangle
# (resim, baslangic, bitis, renk)
cv2.rectangle(img, (0,0), (256,256),(255,0,0), cv2.FILLED)
cv2.imshow("Dikdortgen: ", img)

# cember  circle
# resim, merkez(0yari capina ihtiyacim var 45)
cv2.circle(img, (300,300), 45, (0,0,255))
cv2.imshow("Cember: ", img)

# metin
#(resim, baslangic noktasi, font, kalinligi, renk)
cv2.putText(img, "Resim", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("metin", img)
