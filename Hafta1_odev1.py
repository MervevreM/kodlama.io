###################################################### VERİ TİPLERİ ###############################################################
#
##### Numeric : Integer, Float, Complex, boolean
#
## Integer: Tam sayılar integer sınıfında yer alır. Yazılırken tırnaklara ihtiyaçları yoktur. Tırnak kullanımı sınıflarını değiştirmektedir.
#           Her integer değer farkına uğramadan float'lara çevrilebilir.
#           ÖRN: Kursların süresi, kursiyerin kursu tamamlama yüzdesi.
##  Float: Ondalıklı sayılar float sınıfında yer alır. Floatlar integerlara çevrilebilir fakat ondalıklı kısım 0 dışında,
#          ÖRN: Java script yazılımcı kampındaki ay (1.5 ay)
#           bir sayı ise değer kaybına uğrar. Integerda olduğu gibi tırnak işaretleri gerektirmez. Kullanılırsa pyhton bunu metin zanneder.
##  Complex: (Tam anlamasam da açıklamayı deneyeceğim.)Türkçede hayali sayılara denk gelen sayılardır. Karesi 0'dan küçük olan sayılar,
#           bu gruba girmektedir. Genellikle i ve j harfleriyle gösterilirler. 
#          ÖRN: YOK
##  Boolean: Yalnızca 2 değeri vardır. True ya da False. Karar verme aşamasında kullanılır. İlk hafleri büyük olmak zorundadır. Aksi halde
#           Pyhton bunu metin zanneder. True ve False integer'a çevrilebilen ifadelerdir. True 1, False ise 0 değerindedir. Belki de temelde
#           1 ve 0 oldukları için numeric kısmında yer alıyorlardır. (Böyledir herhalde)
#           ÖRN: (Hiç emin olmamakla birlikte) Kurs tamamlama yüzdesi yüz olunca eklemeyi bırakacak denmiş olabilir arkada. Bu da True False
#           ile yapılmış olabilir. 
#
############  Text: String
#
##     String:Kısaltması str'dir. Her türlü metinsel ifade için kullanılır. Tırnak içerisinde kullanmak gerekmektedir. Aksi halde pyhton 
#             sınıfını anlayamayacaktır. Tırnak içerisindeki her şeyi pyhton string kabul edecektir. Integer'larda yani sayı değişkenlerinde
#             tırnak koymamaya dikkat edilmelidir. Aksi halde istenilen sistem kurulamayacaktır. String ifadelerde İngilizce'de olmayan harflere 
#             yer vermemek daha iyi sonuçlar verecektir. 
#             ÖRN: Her türlü kurs adı, sağda bulunan seçenekler, kategoriler.
#
#
#
########### Sequence (Dizi) : List, Tuple, Set, Dictionary 
# 
##  List: Basitçe listelerdir. Öge koleksiyonları oluşturmamıza olanak sağlar. Güncellenebilir olmaları sebebiyle oldukça kullanışlıdır. 
#          Köşeli parantezle oluşturulur. Her bir değer virgülle ayrılmalıdır. İçerisine karışık olarak her türlü veriyi bir çok kere alabilir. 
#          ÖRN: Tüm kurslarda listelenen kurslar.
##  Tuple: Listelerle aynı özellikleri taşır. Fakat normal parantezle oluşturulur. İçerisine farklı türde ögler alabilir.
#          Her öge virgülle ayrılmalıdır. Düzenli yapıya sahiptir. Her ögenin yeri bellidir bu sebeple aynı ögeden birden fazla alabilir. 
#          Listelerden onu ayıran en büyük özelliği güncellenemez oluşudur.Tuple'lar ilk yapıldığı şekilde kalır.
#          Listeden daha hızlı çalıştırılır. İçeriğinin değiştirilemez oluşu bize neler kazandırdığından çok emin değilim ama tahmin yürüteceğim. 
#          Çoklu projelerde fiks listelenecek ögeleri tuple'da toplamak projenin ilerleyen zamanlarda farklı birinin içeriği değiştirip,
#          sıkıntı çıkarmasını önleyebilir.  
#          ÖRN: Kurs programı
##    Set: Süslü parantezle oluşturulan öge koleksiyonlarıdır. Her ögeden yalnızca bir tane barındırır. Liste ve tuple'larda tanımlanan sıraya 
#          uygun olarak aynı yerlerde aynı ögeler bulunurken set farklı çalışır. Tanımlanan öge tanımlanan yerde bulunmaz karışık olarak 
#          çıktı verir. Öge yerini belirterek işlem yapmak (index) kullanmamıza izin vermez. İçlerinde veriye ulaşmak için oluşturulan 
#          en iyi koleksiyondur. Değiştirilemez yapıya sahiptir. Yalnızca öge silinebilir ya da eklenebilir. İçine str, int bool alabilir.
#          ÖRN: Bilmiyorum :(
##   Dict: Süslü parantezle oluşturulur. İçerisinde anahtar ve değer olarak ikili değer barındırır. İlki anahtar olan key, ikincisi ise
#          değer olan value'dur. Key ya da value kısmına metinsel bir değer vermek istersek tırnak içerisinde yazarız (Her metinsel ifadede 
#          olduğu gibi). Anahtar ve değer arasına iki nokta üst üste (:) işaretini koyarak key value arasındaki köprüyü oluştururuz.
#          Pyhton 3.6 ve öncesinde set'ler gibi düzensizken 3.7 ve ilerisinde düzenli bir yapı kazanmıştır. Setlerdeki gibi her ögeden 1 tane
#          kullanılmasına izin vermektedir. Her key ve value (özgün?) unique'tir.  İçerisine farklı veri tipleri alabilir.
#          ÖRN: Sık sorulan sorular? Her dersin adı ve butonu?



########################################  İİİİFFF

kurslar= ["Java", "Pyhton", "C#"]
kurslarım= ["Pyhton"]
profil= ["Profil sayfasına yönlendiriliyorsunuz"]
tıklama = "?"

if tıklama==kurslar:
    print(kurslar)
if tıklama==kurslarım:
    print("kurslarım")
if tıklama==profil:
    print("profil sayfanıza yönlendiriliyorsunuz")
if tıklama != kurslar or kurslarım or profil:
    print("Şu an hiçbir şey yapmıyorum")








