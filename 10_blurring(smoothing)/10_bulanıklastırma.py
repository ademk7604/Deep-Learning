"""
-  Bulaniklastirma -
- Goruntu bulanikligi, goruntunun dusuk gecisli bir filtre uygulanmasiyla elde edilir
- Gurultuyu gidermek icin kullanislidir. 
  Aslinda goruntuden yuksek frekansli icerigi(ornegin: parazit, kenarlar) kaldirir
- OpenCV, uc ana tur bulaniklastirma teknigi saglar.
    - Ortalama Bualniklastirma
    - Gauss Bulaniklastirma
    - Medya Bulaniklastirma

+ Bulaniklastirmada resim uzerinde bulunan detaylar azaltilir. Detaylar azaltilirken gurultu de azaltir

    - Ortalama Bulaniklastirma -
- Bir goruntunun normallestirilmis bir kutu filtresiyle sarilmasiyla yapilir
- Cekirdek alani altindaki tum piksellerin ortalamasini alir ve bu ortalamayi merkezi oge ile yer degistirir

    - Gauss Bulaniklastirma -
- Bu yontemde kutu filtresi yerine Gauss cekirdegi kullanilir.
- Pozitif ve tek olmasi gereken cekirdegin genisligini ve yuksekligini belirtilir.
- SigmaX ve SigmaY, X ve Y yontemlerindeki standart sapmayi belirmeliyiz.Yani gauss kutucugu bu sekilde olusuyor

    - Medyan Bulaniklastirma -
- Cekirdek alani altindaki tum piksellerin medyanini alir ve merkezi oge bu medyan degerle degistirilir.
- Tuz ve biber gurultusune karsi oldukca etkilidir. (goruntu uzerindeki siyah beyaz noktaciklar)
+ piksellerin medyanini almasi deemek, ortadaki sayiyi aliyor
"""
import cv2
import matplotlib.pyplot as plt # gorsellestirme icin
import numpy as np                # gurultu olusturma icin

import warnings                 # uyarilari ortadan cikarmak icin uyari cikmasi hata demek degildir
warnings.filterwarnings("ignore")

# blurring (detayi azaltir, gurultuyu engeller)
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("original"),plt.show()

"""
Ortalama bulaniklastirma yontemi

"""
dts2 = cv2.blur(img, ksize = (3,3))
plt.figure(),plt.imshow(dts2),plt.axis("off"),plt.title("Ortalama Blur"),plt.show()

"""
- gaussian blur
""" # sigmaY vermedigim zaman x ile esit oluyor
gb = cv2.GaussianBlur(img, ksize= (3,3), sigmaX = 7)
plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("Gauss Blur"),plt.show()

"""
medyan blur
"""
mb = cv2.medianBlur(img, ksize = 3)
plt.figure(),plt.imshow(mb),plt.axis("off"),plt.title("Median Blur"),plt.show()

# noiz e ihtiyacimiz var. resimlerin uzerine koyacagiz

def gaussianNoise(image):
    row,col,ch = image.shape # ch resmimimin 1 mi 2 mi 3 mu oldugu RGB yani
    mean = 0   #ortalama degerimiz 0
    var = 0.05 # varians, sitandart sapmamizdir
    sigma = var**0.5 # var in kare kokudur
    
    gauss = np.random.normal(mean, sigma, (row,col,ch)) #gaussian nin diger ismi normal dagilimdir
    gauss = gauss.reshape(row,col,ch) # boyutundan bir kez daha emin oluyorum.
    noisy = image + gauss # bu sekilde gurultulu resmi elde ediyorum
    
    return noisy
"""
- normal resimde degerler 0 ile 255 rasindadir. 
- Gurultuyu ekleyebilmemiz icin degerleri 0 ile 1 arasina tasimamiz gerekiyor
- eger normalize edilmemis bir goruntunun uzerine eklersek zaten bir sey gozukmeyecektir

"""
# ice aktar normalize et 0 ile 1 arasina tasimak icin /255 e bolunce cekmis olduk
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("original"),plt.show()

# simdi bu normalize edilmis resmin uzerine gaussian ekleyelim
gaussianNoisyImage = gaussianNoise(img)
plt.figure(),plt.imshow(gaussianNoisyImage),plt.axis("off"),plt.title("Gauss Noisy"),plt.show()

# gauss blur
gb2 = cv2.GaussianBlur(gaussianNoisyImage, ksize= (3,3), sigmaX = 7)
plt.figure(),plt.imshow(gb2),plt.axis("off"),plt.title("With Gauss Blur"),plt.show()
# gauss blur ile noisy azaltma islemi gerceklestirdik

#birde tuz karabiber gurultusu olusturarak median blur ile ortadan kaldiralim
# tuz karabiber dedigimiz sey resmin uzerine siyah ve beyaz noktaciklarin rastgele yerlestirilmesi demek


def saltPepperNoise(image):
    
    row,col,ch = image.shape
    s_vs_p = 0.5 # salt ve pepper in orani %50 ye % 50
    
    amount = 0.004 
    
    noisy = np.copy(image) # orjinal guruntumuzu bozmayalim ielrde kullanabiliriz 
    
    # salt beyaz noktaciklari ekliyorum. 
    # ceil(), elimizdeki ondalikli sayiyi yukari veya asagiya tamamliyor. image.size resmimizdeki pixeller
    num_salt = np.ceil(amount * image.size * s_vs_p) # burda resmimiz uzerinde bulunacak beyaz gurultu sayisi
    salt_coords = [np.random.randint(0, i -1, int(num_salt)) for i in image.shape] # koordinatlari belirledik
    noisy[salt_coords] = 1
    
    # pepper siyah noktalar (1 - s_vs_p), burayla beyazlarin toplami 1 olmasi lazim yani birbirini tamamlarlar
    num_pepper = np.ceil(amount * image.size * (1 - s_vs_p))
    pepper_coords = [np.random.randint(0, i -1, int(num_pepper)) for i in image.shape]
    noisy[pepper_coords] = 0
    
    return noisy

spImage = saltPepperNoise(img)
plt.figure(),plt.imshow(spImage),plt.axis("off"),plt.title("SP Image")

# burda karsilastigimiz hata dan sunu anliyoruz OpenCV float64 kabul etmiyor float32 cevir diyor
mb2 = cv2.medianBlur(spImage.astype(np.float32), ksize = 3)
plt.figure(),plt.imshow(mb2),plt.axis("off"),plt.title(" With Median Blur"),plt.show()










