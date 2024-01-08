import cv2

#ice aktarma
img = cv2.imread("messi5.jpg", 0) # 0, gray olarak yani siyah beyaz olarak ice aktarak

#gorsellestirme
cv2.imshow("ilk Resim", img) #resmini ismini ilk Resim yaptik

k = cv2.waitKey(0) &0xFF 

if k == 27: #27=esc ye denk gelmekte
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("messi_gray.png", img)
    cv2.destroyAllWindows()












































































