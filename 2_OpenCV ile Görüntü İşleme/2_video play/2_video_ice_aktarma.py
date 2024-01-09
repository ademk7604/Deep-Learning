"""
-Resim toplulugunu nasil video haline getirecegimizi ogrenecegiz
-Video: resimleri belirli bir periotta art arda aktarmayla olusur.
-
"""

import cv2
import time

#video ismi
video_name = "MOT17-04-DPM.mp4"

#video ice aktar: capture diye gecer, cap olarak kisaltilir

cap = cv2.VideoCapture(video_name)

print("Genislik: ",cap.get(3)) # genislik kodu 3 dur
print("Yukseklik: ",cap.get(4))

# cap' a video_name videosunu yukledim bos olsa bile yukler, 
# acabildimmi diye KONTROL ET bunu yapmazsan cok hata alirsin
# run da hata mesaji gelmedigi icin videomu aktarabildigimi anliyorum
if cap.isOpened() == False:
    print("Hata")

"""
-video yu okuma, frame video nun icerisinde bulunan her bir resimdir
-ret return dur cap.read() okumasi gerceklesmezse ret false doner
-while dongusu ile read() methodu calistirarak bu islemi surekli gerceklestirip 
-resimleri video haline getiriyoruz. 
-Aslinda bu resimlerdir resmi tikladigimizda bu kodlarla video oynuyor
- iki break de video yu kirip cikmamiza yariyor
-birincisi, video artik bitmistir otomatik cikar
-ikincisi artik ben videoyu izlemek istemiyorum kirip cikarim.
"""

while True:
    ret, frame = cap.read()
    
    if ret == True:
        
        time.sleep(0.01) # uyari: kullanmazsak cok hizli akar
        
        cv2.imshow("Video", frame)
    else: break          # okuyamazsam while kirip cikiyor
    
# bu while calisirken biz videoyu izliyoruz ve aktarma devam ediyor
# izlemek istemiyorsak q ile cikis yapiyoruz
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

#cap VideoCapture rini yani almayi birakiyoruz
cap.release() # stop capture
cv2.destroyAllWindows() #tum acik pencereliri kapatiyoruz


    
    
    
    
    
    
    
    
    
    