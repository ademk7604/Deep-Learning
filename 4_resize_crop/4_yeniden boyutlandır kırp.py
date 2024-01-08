# resimleri nasil yeniden boyutlandiracagimizi veya boyutlandiracagimizi ogrenecegiz
# nesne takibinde boyle islemler yapacagiz. 1080 1080 yerine 320 320 bir resim ile calismak dava verimli olabilir
# suankiu resim RGB color
import cv2

img = cv2.imread("lenna.png") 
# Resim boyutu:  (512, 512, 3) sifirsiz bastigimizda(aslinda orda gizli 1 var) renkli hali geliyor
print("Resim boyutu: ", img.shape)
cv2.imshow("Original", img)

#resized
imgResized = cv2.resize(img, (800,800))
print("Resized Img Shape: ", imgResized.shape)
cv2.imshow("Img Resized", imgResized)


# kirp Cropped
imgCropped = img[:200,:300] # width height -> ama OpenCV de bu tam tersi height width
cv2.imshow("Kirpik Resim", imgCropped)