# %% spyder tanitimi

# %% degiskenler

tamsayi_degisken=10
ondakili_sayi =12.3
print(tamsayi_degisken)

# 4 islem ozellikleri

pi_Sayisi = 3.14
katsayi = 2

toplam = pi_Sayisi + 1
fark = pi_Sayisi -1
carpma = pi_Sayisi*katsayi
bolme = pi_Sayisi/katsayi

# print
print("Toplam", toplam)
print("Toplam: {} ve fark: {}".format(toplam, fark))
print("Carpma: %.1f, bolme: %.4f" % (carpma, bolme))

# degiskenler arasi donusum
carpma_int = int(carpma)
print(carpma_int)

tamsayi_float = float(tamsayi_degisken)
print(tamsayi_float)

string = "mergaba dunya"
print(string)

resim_yolu = "veri" + "\\"+ "img"+".png"
print(resim_yolu)

# %% python temel sozdilimi
# buyuk ve kucuk harf

temel = 6
TEMEL = 7

# yorum
"""
bu bolumde soz dizimi calisiyoruz
    - buyuk kucuk harf
    - yorum
    - girinti
    -anahtar kelimeler
"""
#girinti
if 5<10:
    print("yes")
else:
    print("no")

#anahtar kelime
de = 4

# def = 4

sayi1 = 5
sayi2 = 2

# 1sayi = 7

# %% liste
"""
-bilesik veri turudur ve cok yonludur
-[1, "a", 1.0]
-farkli veri tiolerini icerisinde  barindirabilir
"""
liste = [1,2,3,4,5,6]
print(type(liste))

hafta = ["pazartesi", "sali","carsamba","persembe","cuma","cumartesi","pazar"]
#ilk eleman
print(hafta[0])

#son eleman
print(hafta[6])
print(len(hafta)) # eleman sayisi
print(hafta[len(hafta)-1])
print(hafta[-1]) # 0. index ilk elemanimizdi -1 demek listenin sonuna git

#liste 2-3-4 elemanlarini yazma 1,2,3 indexs yaz son eleman dahil degildir
print(hafta[1:4]) # 1 den 4 e kadar 1 dahil 4 dahil degil

# sayi listesi
sayi_listesi = [1,2,3,4,5,6]
sayi_listesi.append(7)
print(sayi_listesi)
#listeden eleamn cikarma
sayi_listesi.remove(4)# burdaki elemani cikariyoruz
print(sayi_listesi)

#listeyi ters cevir
sayi_listesi.reverse()
print(sayi_listesi)

#listeyi sirala
sayi_listesi = [1,3,2,4,5,67,0]
sayi_listesi.sort()
print(sayi_listesi)

# %% tuple
"""
degistirilemez ve sirali bir kolleksiyon tipidir.
(1,2,3)
salt okunur listeler de olusturlabilirler
"""

tuple_veritipi = (1,2,3,3,4,5,6)
#ilk elemani
print(tuple_veritipi[0])

#ilikci indexten sonraki elemanlari yazdir
print(tuple_veritipi[2:])

# count eleman
print(tuple_veritipi.count(3))

tuple_xyz = (1,2,3)
x,y,z = tuple_xyz
print(x,y,z)

# %% deque
"""
listelere cok benzerler, listelerde bir liste olusturulurken 
listenin boyutunu tanimlamiyorduk
deque de listenin boyutunu tanimlayabiliyim circle bir liste seklinde 
liste olusturmamiza imkan veriyor
bilgisayar biliminde cift uclu kuyruk yani circle olarak adlandirilabilir
onden veya arkadan elemanlarin eklenebildigi ve cikartilabildigi bir yapidir
listeye benziyor ama listeden farki boyutunun onceden belirleniyor olmasi
""" 

from collections import deque
dq = deque(maxlen = 3)

dq.append(1) # 1 ekle sonuna [1]
print(dq)

dq.append(2) # 1 ekle sonuna [1,2]
print(dq)

dq.append(3) # 1 ekle sonuna [1,2,3]
print(dq)

dq.append(4) # boyutu 3 oldugu icin basindakini cikardi [2,3,4]
print(dq)


dq = deque(maxlen = 3)
dq.append(1) # 1 ekle sonuna [1]
print(dq)
dq.append(2) # 1 ekle sonuna [1,2]
print(dq)

dq.appendleft(3) # 1 ekle sonuna [3,1,2]
print(dq)

dq.clear()
print(dq)
#pop ozelligi son elemani cikarir
# Bir deque oluştur
my_deque = deque([1, 2, 3, 4, 5])

# Son elemanı deque'den çıkar
popped_element = my_deque.pop()

print("Çıkarılan eleman:", popped_element)
print("Güncellenmiş deque:", my_deque)
#copy iozelligi
copied_my_deque = my_deque.copy()
my_deque.append(6)

print("my deque:", my_deque)
print("Kopya deque:", copied_my_deque)

# %% sozlukler
"""
- bir cesit karma tablo turudur. bir cok types
- pandas kutuphanesinin  temlini olusturur
- anahtar ve deger ciftlerinden olusurlar
-anahtar dedigimiz her typ olabilir
-{"anahtar": deger}
"""
dictionary = {
    "istanbul": 34,
    "izmir" : 35,
    "konya" : 42}
print(dictionary)

# istanbul anahtarinin degeri
print(dictionary["istanbul"])

#anahtarlar
print(dictionary.keys())

#degerler
print(dictionary.values())

# history = dict["val_loss", "val_acc","loss","acc"]
#ilerde bu sekilde bunu kullanacagiz

# %% kosullu ifadeler if else statement
"""
bir bool ifadesine gore dogru yada yanlis olarak degerlendirilmesine
bagli olarak farkli hesaplamalar ve eylerler gerceklestiren bir ifadedir
"""
#buyuk kucuk sayi karsilastirilmasi
sayi1 = 12.0
sayi2 = 20.0

if sayi1 < sayi2:
    print("sayi 1 kucuktur sayi2")
elif sayi1>sayi2:
    print("sayi 1 buyuktur sayi2")
else:
    print("sayi1 esittir sayi2")
    
liste = [1,2,3,4,5]
deger = 1

if deger in liste:
    print("{} degeri listenin icerisindedir".format(deger))
else:
    print("{} degeri listenin icerisinde degildir".format(deger))

dictionary = {"Turkiye": "Ankara", "Ingiltere": "Londra", "Ispanya":"Madrid"}
keys = dictionary.keys()
deger = "Turkiye"
if deger in keys:
    print("Evet")
else:
    print("Hayir")
    
bool1 = True
bool2 = False
#or ikisinden biri dogru oldugunda true
if bool1 or bool2: print("Dogru")
else: print("Yanlis")

bool1 = True
bool2 = False
#and her ikisi true veya false ise true ama birbirinden farkli iseler false doner
if bool1 and bool2: print("Dogru")
else: print("Yanlis")


# %% donguler
"""
-bir dizi uzerinde yenileme yapmak icin kullanilan yapilardir.
-diziler: liste,tuple, string, sozluk, numpy pandas veri tipleri olabilir
"""

#for
for i in range(1,11):
    print(i)

liste = [1,4,5,6,8,3,3,4,67]
print(sum(liste))


toplam = 0
for c in liste:
    toplam = toplam +c
    print(c)
print(toplam)
#bu sekilde calismalarimiz olacak
tup1 = ((1,2,3),(3,4,5))
for x,y,z in tup1:
    print(x,y,z)
    
#While
i = 0
while i < 4:
    print(i)
    i= i + 1

liste = [1,4,5,6,8,3,3,4,67]
sinir = len(liste)

her =0
hesapla = 0
while her < sinir:
    hesapla = hesapla + liste[her]
    her = her +1
print(hesapla)

# %% fonksiyonlar
"""
- karmasik islemleri toplar ve tek adimda saglar
-sablon
-duzenleme
"""
## fonksiyonlari tipleri building fonk ve user defaend fonk diye
# kullanici tarafindan tanimlarnan fonk. - user defaend fonk

def daireAlan(r): #(classs larin icinde kullaniliyorsa method bu sekilde funski denir bunlara)
    """
    Parameters
    ----------
    r : int - daire yaricapi.

    Returns
    -------
    daire_alani: float -daire alani
    """
    pi = 3.14
    daire_alani = pi*(r**2)
    
    #print(daire_alani)
    
    return daire_alani # veriabel i methodun disina veriyor

daireAlaniDegiskeni = daireAlan(3)
# bundan sonra methodda yaptigim degeri istedigim yerde kullanabiliyorum
print(daireAlaniDegiskeni)


#ilerde DERIN ogrenmede learning read diye bir parametresi var onu fonk parametresinde 
#default olarak tanimliyoruz ayri gonderdigimiz method parametresinde degistirebiliyoruz
# pi gibi lr = 0.001 olarak kullaniyoruz. degistirmek gerekirse daireCevresi(3,lr = 0.001)
def daireCevresi(r, pi =3.14):
    """
    Parameters
    ----------
    r : int - daire cevresi.
    pi: float - pi sayisi

    Returns
    -------
    daire_cevresi: float -daire cevresi
    """
    
    daire_cevresi = 2*pi*r
    
    return daire_cevresi

daireCevre = daireCevresi(3,5)
print(daireCevre)

    
# demin sadece return ile veriable yi disari aktarabiliyoruz demistik aslinda baska yoluda var
# ornegin, veriable yi disarda tanimlayip 
#methodun icinde global katsayi olarak kullandigimda veriableyi heryerde kullanabilirim
katsayi = 5
def katsayiCarpani():
    global katsayi
    print(katsayi*katsayi)

katsayiCarpani()
print(katsayi)

#bos fonksiyonlar
"""
Neden bos fonk kullaniyoruz sacma degilmi?
bazi kutuphanelerde imput olarak fonk aliniyor ve bu fonksiyon bizim
kullanmak istedigimiz birsey degil AMA
kutuphanenin soz dizimi nedeniyle buraya bu fonks yazmak zorundayiz
"""
def bos(): # bu sekilde calistirdigimizda hata verir bunun icin altina pass yaziyoruz
    pass

# built in fonk.
liste = [1,2,3,4]
print(len(liste))
print(str(liste))
liste2 = liste.copy()
print(liste2)
print(max(liste2))
print(min(liste))

#lambda fonk
"""
-ileri seviyeli 
-kucuk ve anonim bir islemdir
"""

def carpma(x,y,z):
    return x*y*z
sonuc = carpma(2,3,4)
print(sonuc)

#ayni islem with Lambda
fonksiyon_lambda = lambda x,y,z : x*y*z
sonuc2 = fonksiyon_lambda(2,3,4)
print(sonuc2)


# %%yield
"""
-yield lin ne oldugunu ogrenebilmemiz icin once generatorun ne oldugunu 
anlamamiz lazim generator u da anlamak icin itearatorun anlamak lazim
- iterasyon -yineleme
-generator
-yield
"""

liste = [1,2,3] # elemanlari tek tek okumak yineleme demektir
for i in liste:
    print(i)
# bu yineleme de veri cok buyukse bunu memori de tuttugumuiz anlamina gelir
# bu bizim istedigimiz birsey degildir. Bunu cozebilmek icin generator yenileyicilerini kullaniyoruz
"""
generator yineleyicileri
generator tum degerleri bellekte saklamaz. Yeri gelince aninda uretirler.
Buda bize milyonlarca resim verisi kullanacagimiz zaman avantaj saglar.
zaten milyonlarca bir veriyi bir listeye aktarirsak bilg. bellegi dolar bilg kapanir
"""

generator = (x for x in range(1,4))
for i in generator:
    print(i)
# birer biorer generator ediyor

#yield, islemin bir generator islemi dondurmesi disinda return gibi kullanilan bir anahtar sozcuktur
"""
fonksiyon eger return olarak generator dondurecek ise bunu return yerine
yield anahtar sozcugu ile yapar. (ceneretir)
"""
def createGenerator():
    liste = range(1,4)
    for i in liste:
        yield i
        
generator = createGenerator()
print(generator)

for i in generator:
    print(i)

# %% numpy "numerical Python" (sayısal Python) :)
"""
- Numpy kutuphanesi, python dili programlama icin bir kutuphanedir
- Buyuk, cok boyutlu diziler ve matrixler icin hesaplama kolayligi saglar
- matrisler icin hesaplama kolayligi saglar 
- (listeler gibi de dusunebiliriz ama listeler de cok fazla fonksiyon yok)
- numpy da cok fazla fonksiyon var.
- Numpy aslinda bir array yapisidir.
"""
# np olarak kisatip kullanacagim
import numpy as np 
# 1 boyutlu numpy dizisi oluştur
arr = np.array([1, 2, 3, 4, 5])

# Diziler arası matematiksel işlemler
result = arr * 2

# Matris oluşturma
matrix = np.array([[1, 2], [3, 4]])

# Matris çarpımı
product = np.dot(matrix, matrix)

print(result)
print(product)

# 1*15 boyutunda bir array-dizi olusturalim
dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dizi)

print(dizi.shape) # array' in boyutu

# 1,15 boyutundaki array imi vektoprumu bir iki boyutlu bir matris haline cevirmek 
# bunun icin 15 3 ile 5 in kati oldugu icin 3,5 lik bir maris haline cevirebilirim

#iki boyutluya cevirelim
dizi2 = dizi.reshape(3, 5)

# verinin ozelliklerini ogrenelim
print("Sekil: ",dizi2.shape)
print("Boyut: ",dizi2.ndim)
print("Veri tipi: ",dizi2.dtype.name)
print("Boy: ",dizi2.size)

#elimizde olan bir resmi veriyi icerige aktardigimiz zaman numpy array olarak
#depolayabiliriz ve bu resmin yani verinin OZELLIKLERINI bilmemiz gerekiyor
#cunku ozelliklerini bilmedigimiz bir verinin nesne siniflandirma, takipte yada 
#tespitinde kullanacagimiz fonksiyonlarin icerisine yolladigimiz zaman buyuk ihtimal hata cikacaktir
# elimize gelecek veri muhakkak bozuk olacaktir yukaridaki gibi 
#Sekil, Boyut, Veri tipi vey boy ozelliklerine bakmamiz lazim

"""
reshape fonksiyonu, bir diziyi yeni bir şekilde düzenlemek veya yeniden 
yapılandırmak için kullanılır. 
Bu işlev, veri yapısının boyutlarını değiştirmenizi sağlar. 
Özellikle, bir dizi veya matrisin boyutlarını değiştirmek için sıklıkla kullanılır.
Örneğin, reshape(3, 5) ifadesi, mevcut bir diziyi (ya da matrisi) 3 satır 
ve 5 sütun olacak şekilde yeniden yapılandırır. Bu işlem, dizinin elemanlarını 
aynı tutarak, ancak farklı bir yapıda düzenleyerek yapılır. 
Yeniden yapılandırılan dizi, önceki diziyle aynı sayıda elemana sahip olmalıdır.
"""

# array type verinin type ni bilmiyorsak bu sekilde ogreniyoruz
print("Type: ",type(dizi2))

#2 boyutlu array
#Yani, 2 boyutlu bir dizi, satırların ve sütunların bir matris veya tablo olarak düzenlendiği bir yapıdır. 
dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])
print(dizi2D)
print(dizi2D.ndim)

# iki boyutlu sifirlardan olusan bir array(matris) olusturalim
sifir_dizi = np.zeros((3,4))
print(sifir_dizi)
"""
- sifirlardan olusan matris olusturmak elde etmek cok onemli
- aslinda burda her bir 0 degeri bir pixel e karsilik gelen genlik degeri vardir
- Bunu daha cok goruntu islemede anlayacagiz.
- Yada education diye bir kavram var siz bir dizi yi basta olusturmayip for
- dongusu icerisinde diziyi olusturmaya kalkarsaniz bu memorinizde cok yer kaplar
- Ama basta boyle sifirlardan olusan bir matris, dizi yada array olusturusaniz
- sonradan bu dizinin icerisini istedigimiz degerlerle doldurmak isterseniz bu 
- memoride cok yer kaplamaz bizim icin avantaj olur
"""

# birlerden olusan bir array
bir_dizi = np.ones((3,4))
print(bir_dizi)

# bos array sifira ne kadar yakinsa bos dur
bos_dizi = np.empty((3,4))
print(bos_dizi)

# arange(x,y,basamak) x ten baslayip y ye kadar basamak basamak sayiyor y dahil degil
dizi_aralik = np.arange(10,50,5)
print(dizi_aralik)

# Linspace(x,y, basamak), x ve y dahil aradaki sayilari basamaga bolmus
dizi_bosluk = np.linspace(10, 20, 5)
print(dizi_bosluk)

# float array, data type kendim belirleyecegim bir array olusturmak istiyorum
float_array = np.float32([[1,2],[3,4]])
print(float_array)

#matematiksel islemler
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2) #diziyi kendisi ile carptik

# dizi elemani toplama
print(np.sum(a))

#max deger
print(np.max(a))

#min deger
print(np.min(a))

#max deger
print(np.max(a))

#meam ortalama
print(np.mean(a))

#median ortadaki sayi
print(np.median(a))

#rastgele sayi uretme [0,1] arasinda surekli uretiriz. uniform 3*3
rastgele_dizi = np.random.random((3,3))
print(rastgele_dizi)
# goruntu uzerinde hata (noiz dedigimiz) bulunabilir bunlari kameranin acisindan,
# nesnenin hizindan olabilir, isik, golgeler olabilir biz bunlari noiz oalark adlandiriyoruz
# goruntu islemede noiz lari ayiklama diye bir kavram var.Biz goruntuler uzerinde rastgele
#yontemi olusturarak hatalar olusturacagiz, sonrada bu hatalari birlikte nasil ayiklayacagimizi
# ogrenecegiz.

# indexs
dizi = np.array([1,2,3,4,5,6,7])
print(dizi[0])

#dizinin ilk 4 elamani
print(dizi[0:4])

#dizinin tersini alalim. Listelerde yaptigimiz reverse n karsiligi
print(dizi[::-1])

# 2 satir 5 stundan olusan bir matris yapalim
dizi2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2D)

#dizinin 1. satir ve 1. sutununda bulunan elemani (index olarak dusun)
print(dizi2D[1,1])

# dizinin tum satirlar ve 1. sutun
print(dizi2D[:,1])

#satir 1, sutun 1,2,3 alalim
print(dizi2D[1,1:4])

# dizinin son satir tum sutunlari
print(dizi2D[-1, :])

# dizimizi nasil vektor haline getirebilecegimizi ogrenelim


dizi2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2D)
#vektor haline getirme
vektor = dizi2D.ravel()
print(vektor)
# Resme ait feature yani ozellikleri cikardiktan sonra bu ozellikleri kullanarak 
#siniflandirma yapacagiz. Bu ozellik katmanlarinin en sonunda bizim siniflandirma
#yapabilecek olan run et vektorune giris yapabilmek icin bir vektor e ihtiyacimiz var
# bu nedenle en sonda bir resmi vektor haline getirmemiz gerekiyor.
# Resimlerde bildigimiz gibi en az iki boyutlu oldugu icin yani rengi de isin icine giriyorsa
# 3 boyutlu. rengi olmadigini varsayalim resim dedigimiz sey iki boyutlu dur. x ve y
# Bu resimleri duzlestirmemeiz gerekiyor duzlestirmek icin bunu yapmak gerekiyor sonra
# bunu siniflandirmaya sokup resmimizin ne oldugunu anlayacagiz. BUNU IYI OGREN ARASTIMA YAP

#
maksimum_sayinin_indeksini = vektor.argmax()
print(maksimum_sayinin_indeksini)

# %% pandas
"""
- Veri isleme ve analizi icin python dilinde yazilmis bir yazilim kutuphanesidir
- Bu kuth. de temel olarak zaman etiketli serileri ve sayisal tablolari icin
- bir veri yapisi olusturulur. Ve bu sekilde veriler cesitli islemlerden gececek
- veri yapisinin icerisine kolay bir sekilde gerceklestirilebilir

+ hizli, guclu(hem arkasinda guclu bir kominitisi var hemde kullandigi methodlarin 
               cakilmasi gibi bir durum olmuyor)
 ve esnek(bize sagladigi farkli method lar sayesinde bazi 
 seyleri yapamasakda cevresinden dolanma gibi esneklik sagliyor islemizi kolaylastiriyor)
 - pandas sayesinde CSV ve text file larini kolayca okuyabiliyoruz. 
 - Bir resmin yaninada muhakkak CSV veya text file olacakki bize resim hakkinda bilgi versin
 - Ornegin bir kedi resminde, kedinin koordinatlarini belirten ve bu koordinatlarda bulunan
 - kedinin veya baska bir nesnenin ne oldugunu belirten bir etikete ihtiyacimiz var. 
 - bunlar da genelde CSV ve text dostyalarinda oluyor.
 - Bizde bunlari pandas sayesinde kolay bir sekilde okuyabiliyoruz
 - Sonrasinda veri biliminde icesinde bulunan eksik verileri cikarmada pandas 
 - kutuphanesi isimizi kolaylastiriyor.
"""

import pandas as pd

# sozluk olustur
dictionary = {"isim" : ["ali","veli","murat","ayse","hilal"],
              "yas"  : [15,16,17,33,45,66],
              "maas" : [100,150,240,350,110,220]}
veri = pd.DataFrame(dictionary)
























































































