# Testlerin açıklamaları
Öncelikle gerekli importları gerçekleştirdim sonrasında bir class oluşturdum.

## Empty_username_password fonksiyonu
driver adında bir değişken oluşturup saucedemo sayfasına gidip sayfayı maximize ettim. username ve password kısmına dokunmadan login butonunu bulup tıklattım. sonrasında ekranda beliren uyarı mesajını locator ile bulup içerisindeki texti alıp olması gereken texti magic string ile assertledim. Bu işlemleri yaparken önceden importladığım sleep ile sistemi belirlediğim saniye kadar uyuttum ki sayfanın henüz yüklenmemesi durumunda sonrasında istediğim işlemi yapamayıp kodun hata vermesi ihtimalinden kurtuldum. (Dezavantaj olarak ise sayfa açıldığı halde beklediğim yerler oldu ve zaman kaybettim.)

## empty_password fonksiyonu
ilk fonksiyondaki gibi driver değişkeni oluşturup sayfaya gittim ve sayfayı maximize ettim. Username kısmını locator ile bulup içerisine magic string ile yazmasını istediğim şeyleri gönderip password kısmını boş bırakarak tekrar locator ile login butonunu bulup tıklattım. Çıkan uyarı mesajını ise locator ile buldurup .text ile olması gerekn yazı ile assertledim.

## locked_out fonksiyonu
Sayfa açma işlemlerini tekrar ettikten sonra username kısmına yine magic stringle veri gönderdim fakat bu sefer kilitli olan kullanıcı adını girip locator ile password alanını buldurup send.keys ile şifreyi gönderdikten sonra login butonuna bastırdım. Çıkan uyarı mesajını yukarıda belirttiğim işlemlerdeki gibi assertledim.

## icon_x fonksiyonu
Bu fonksiyonu yapabilmek adına epey uğraştım. Sayfa açılış kısmını aynı şekilde ilerlettikten sonra öncesinde (yani visible iken) x iconlarının locatorlarını aldım. Sonrasında hata almamak adına try except yapısı ile x iconlarını buldurmayı denedim. Bulamaması olumlu olandı bu sebeple except kısmında her şeyin yolunda olduğu mesajını ekledim. Ardından send.keys ile hiçbir şey göndermeyerek direkt olarak login butonuna bastıktan sonra username ve password alanında bulunan iconların çıkıp çıkmadığını if yapısında iconlara .isplayed ile çıkıp çıkmadıklarını kontrol ettim çıktıysa olumlu mesaj bıraktım çıkmadıysa yani else durumunda ise olumsuz mesaj bıraktım. Login butonunun yanında çoktan çıkmış olan uyarıyı kapatma butonunu ise locator ile buldurup tıklattırıp tekrardan try except ile x iconlarının varlığını kontrol ettim.

## Page fonksiyonu
Giriş işlemlerini tekrar edip username ve password kısımlarına kullanıcı adı ve şifre göndermenin ardından login butonuna bastırdım ve açılan sayfanın url'ini .current_url ile bir değişkene atadım. Olmasını istediğim url'i de bir başka değişkene atamanın ardından iki url'i assertledim.

## Does_Inventory_have_six_items fonksiyonu
Sayfaya giriş kısımlarını tekrarlamanın ardından username ve password kısmına kullanıcı adı ve şifreyi gönderip inventory kısmındaki ürün listesine locator ile ulaşıp bunu bir değişkene atadım. Olmasını istediğim ürün sayısı olan 6'yı if ile len() kullanarak kontrol edip 6 ise olumlu mesaj 6'dan farklı ise olumsuz mesaj gönderdim.


## Farkettiklerim
Sürekli sayfa açmak için aynı şeyleri tekrarladım locatorları sürekli tekrarladım bu tekrarlar zamanımı aldı ve kodda kalabalık bir görüntü oluşturdu.