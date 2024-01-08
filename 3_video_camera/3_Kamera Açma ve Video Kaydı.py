# veri toplama acisindan onemli, kendi verimizi nasil toplayip kaydedecegimizi ogreniyoruz
import cv2

cap = cv2.VideoCapture(0) # 0 kamera icin yazdik

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width,height)

#video kaydet. fourcc() dedigimiz sey cevceveleri sikistirmak icin 
#kullandigimiz 4 karakterli kodek kodu bu windows icin ama Linux ve mac de farklidir
# 20, Frame for second yani her saniyede gorecegimiz resim sayimiz yani video hizimiz
writer = cv2.VideoWriter("video_kaydi.mp4", cv2.VideoWriter_fourcc(*"DIVX"),20,(width, height))

while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)

    #save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
writer.release()
cv2.destroyAllWindows()
