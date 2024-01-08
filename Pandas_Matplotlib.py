
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
dictionary = {"isim" : ["ali","veli","kenan","murat","ayse","hilal"],
              "yas"  : [15,16,17,33,45,66],
              "maas" : [100,150,240,350,110,220]}
veri = pd.DataFrame(dictionary)
print(veri)


#ilk 5 satir
print(veri.head())
print(veri.columns)
#veri bilgisi
print(veri.info())

# verinin icnde bulunan sayisal degerlerin istatistiksel ozelliklerine bakalim
print(veri.describe())

#yas sutunu
print(veri["yas"])

#sutun eklemek
veri["sehir"] = ["Ankara","Istanbul","Konya","Izmir","Bursa","Antalya"]
print(veri)


#Yas Sutunu
print(veri.loc[:,"yas"])

#Yas Sutunu ilk 3 satiri
print(veri.loc[:2,"yas"])
#print(veri.loc[:3,"yas"]) burada numpy dan farkli oluyor 3 inklusive oluyor o yuzden 2

#yas ve sehir arasindaki stunlar ve ilk 3 satir
print(veri.loc[:2,"yas":"sehir"])

#isim ve yas arasi sutunu ve 3 satiri alalim
print(veri.loc[:2,["isim","yas"]])

#satirlari tersten yazdir
print(veri.loc[::-1,:])

#yas sutunu with iloc (yani index loc yazdiracagiz)
print(veri.iloc[:,1])

# ilk 3 satir ve yas ile isim stunlarini yazdiralim
print(veri.iloc[:3,[0,1]]) #[0,1] index olarak belirtirken boyle yapiyoruz
#:3 bu sefer ilk 3 deyince exklusive oldu pandas kutuphanesinde boyle belirlenmis degisiyor :)


dictionary = {"isim" : ["ali","veli","kenan","murat","ayse","hilal"],
              "yas"  : [15,16,17,33,45,66],
              "sehir": ["Izmir","Ankara","Konya","Ankara","Ankara","Antalya"]}
veri = pd.DataFrame(dictionary)
print(veri)

# ilk olarak yasa gore bir filtre yas >22
filtre1 = veri.yas > 22
filtrelenmis_veri = veri[filtre1]
print(filtrelenmis_veri)

#ortalama yas
ortalama_yas = veri.yas.mean()

# yeni bir yas grubu oluturuyoruz. list comprehension yazacagiz
veri["YAS_GRUBU"] = ["kucuk" if ortalama_yas > i else "buyuk" for i in veri.yas]
# sinteks biraz karisik gelebilir ama mantigini bu sekilde ezberlenebilir
print(veri)

#ikiveri setini yatayda ve dikeyde birlestirmeyi ogrenelim
# iilerde goruntu islemede karsilastigimiz bazi verileri birlestirmemiz gerekecek
#birlestirme

sozluk1 = {"isim" : ["ali","veli","kenan"],
           "yas"  : [15,16,17],
           "sehir": ["Izmir","Ankara","Konya"]}
veri1 = pd.DataFrame(sozluk1)

#veri seti 2 olusturalim
sozluk2 = {"isim" :["murat","ayse","hilal"],
           "yas"  :[33,45,66],
           "sehir":["Ankara","Ankara","Antalya"]}
veri2 = pd.DataFrame(sozluk2)

#Dikeyde birlestirme yapalim concat
veri_dikey = pd.concat([veri1, veri2], axis = 0)
# alt alta  birlestirmis oluyorum

#yatay birlestirme, ayni stunlara sahip oldugu icin burda cok mantikli olmadi
veri_yatay = pd.concat([veri1, veri2], axis = 1)
#farkli sutunlardan ise yatayda birlestiriyoruz ayni stunda ise dikey de


# %% matplotlib kutuphanesi
"""
+ gorsellestirme
- Bu ktuph ile hem islenmis hemde islenmemis goruntulerimizi gorsellestirecegiz
- Hem nesne takibinde hem tespitinde hemde siniflandirma sonucunu ortaya cikarmis oluruz
-  verilerdeki degerleri kullanabilir patern leri ortaya cikarabiliriz
- matplotlib ktuph amaci numpy kutupjhanesi ile elde ettigimiz matriks leri gorsellestirmektir
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([4,3,2,1])
plt.figure() # figur e acma
plt.plot(x, y, color="red", alpha = 0.7, label = "line") # saydamlik alpha
plt.scatter(x,y,color = "blue", alpha=0.4, label = "scatter") # scatter sacilim, mavi topcuklar
plt.title("Matplotlib")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True) # arka plan kare cizgileri
plt.xticks([0,1,2,3,4,5])
plt.legend() #label in gozukmesi icin bu fonksiyonu cagirdik
plt.show() # figur e kapatma show demezsem sonraki calistiracagimiz grafiklerle karisabilir

fig, axes = plt.subplots(2,1, figsize=(9,7)) # 2,1 2 satir 1 stun olacak sekilde 2 grafik
fig.subplots_adjust(hspace = 0.5) #hspace iki grafik arasi mesafe

x= [1,2,3,4,5,6,7,8,9,10]
y= [10,9,8,7,6,5,4,3,2,1]

axes[0].scatter(x,y)
axes[0].set_title("sub-1")
axes[0].set_ylabel("sub-1 y")
axes[0].set_xlabel("sub-1 x")

axes[1].scatter(y,x)
axes[1].set_title("sub-2")
axes[1].set_ylabel("sub-2 y")
axes[1].set_xlabel("sub-2 x")






























































