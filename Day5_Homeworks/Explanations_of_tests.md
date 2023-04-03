# Explanations of tests

Kullanılacak importları gerçekleştirdim class oluşturdum fonksiyonları bu classa ait olarak yazdım.

## Farkettiklerim

Öncelikle bir önceki fonksiyonlarla bu fonksiyonu kıyaslamak istiyorum. Class yapısını öğrenmeden önce her fonksiyonun başında önce driver tanımlayıp sonra istediğim sayfayı yazıp sonra sayfayı büyütüyordum. Class, ortak olan her şeyi bir yerde saklayıp her seferindeaynı şeyleri yazmaktan kurtardı. Webdriverwait ise sleep'te oluşan boşa zamanlardan kurtulup testimizi daha hızlı işler hale getirmemize olanak sağladı. 

## setup fonksiyonu

Bu fonksiyon class yapısı içerisindeki her fonksiyondan önce çalışan class tarafından otomatik oluşturulmuş bir fonksiyondur. Her fonksiyonda ilk olarak yaptığımız ortak işlemleri burada kullanarak diğer fonksiyonlarda sürekli aynı işlemleri yapmaktan kurtulacağımız için istediğimiz sayfaya giderken kullanacağımız işlemleri burada tanımladım. Ek olarak günün tarihini kendi adı olarak alacak bir klasör adı değişkeni oluşturdum. Bu değişkenle de işlem yapılan günün adıyla klasör oluşturacak eğer bu isimle klasör varsa yenisini oluşturmayacak bir yapı kurdum. Ayrıca her fonksiyonun screenshot'ı ise ilgili günün klasörüne fonksiyonun kendi ismiyle .png olarak kaydedilecek.

## teardown fonksiyonu

Bu fonksiyon ise class içerisindeki her fonksiyonun ardından çalışan fonksiyondur ve class oluşturulunca otomatik olarak oluşturulur. Bunun içerisine de sayfanın kapanması işlemini yazarak her fonksiyonun ardından açılan sayfanın kapanmasını sağladım.

## Wait_for_element fonksiyonu

Sleep'te yaşadığımız zaman kaybının önüne geçen bu yapıyı her fonksiyonda birçok kez kullandığımız için daha kısa bir isimle tanımladım. İçerisine beklenecek elementin locatorını yazarak ilgili yerlerde kullandım.

## test_empty_username_password fonksiyonu

önce setuptaki sayfa açma işlemimiz gerçekleşti ardından önceden tanımladığım bekleme fonksiyonuna login butonunun görünmesini bekleyip direkt tıklattım. Tekrar bekleme işleminden sonra altta çıkan uyarı mesajını buldum. Assertleme işleminden hemen önce sayfanın sreenshot'ını alıp dosyaya ekledikten sonra metni assertledim.

## test_empty_password fonksiyonu

Setuptaki işlemler tamamlandı. username kısmını buldurup tıklattım. Yeni öğrendiğimiz actions chains'i importlarken as actions yazığım zincirleme işlemlerimi bununla kullandım. Actions içerisinde elemente gelip üzerine tıklayıp kullanıcı adını magic string ile gönderdim (perform kullanark). Ardından login butonunu bulup tıklattım. Çıkan uyarı mesajını değişkene .text ile içerisindeki yazı ve beklenilen mesajı assertlemeden önce bu fonksiyonun screenshot'ını almak için önceden tanımladığım yapıyı kullandım.

## test_locked_outfonksiyonu

Username kısmını bekledim actions kullanarak username kısmını buldum kilitli kullanıcının adını yazıp password kısmını bulup şifreyi gönderebileceğim işlem zincirlerini oluşturup perform ettim. Çıkanuyarı mesajı ve beklenen mesaj assert'ünü yapmadan önce screenshot alıp mesajları karşılaştıran assert'ü kullandım.

## test_icon_x fonksiyonu 

Önceden aldığım x iconlarının locator'larını try veexcept ile varlığını kontrol etmenin ardından login butonunu bulup tıklattım. Sonrasında x iconlarını değişkene atayıp if yapısıyla .isplayed kullanarak görüntülenip görüntülenmediğini kontrol ettim. Ardından Uyarı mesajında bulunan kapatma butonuna tıklatarak tekrar try except yapısıyla kontrol ettim. Son olarak ise screenchot'ları almasını sağlayan yapıyı kullandım.

## test_page fonksiyonu

Setup fonksiyonundaki işlemlerin olmasının ardından username kısmını buldurup tıklatıp kullanıcı adını giren bir işlem zinciri oluşturdum ve perform ettim. Ardından password kutucuğu için de aynı şeyleri yapıp şifreyi gönderip perform ettim. Ardından İçerisinde bulunulan sayfanın url'ini alacağım current_url işlemi ile bir değişken oluşturup beklenen url ile assert'ledim. Tabi assertlemeden hemen önce sayfanın screenshot'ını alan yapıyı kullandım.

## test_Does_Inverntory_have_six_items fonksiyonu

Setup fonksiyonundaki işlemlerin olmasının ardından username kısmını buldurup tıklatıp kullanıcı adını giren bir işlem zinciri oluşturdum ve perform ettim. Ardından password kutucuğu için de aynı şeyleri yapıp şifreyi gönderip perform ettim. İnverntory'de bulunan itemlerin olacağı bir değişken tanımladım ve beklenen ürün sayısı olan 6 ile asserlemeden önce sayfanın screenshot'ını alan yapıyı kullandım ve assert işlemini gerçekleştirdim.

## test_add_to_cart fonksiyonu 

Setup fonksiyonunun ardından önce problem_user isimli kullanıcının giriş sağlaması için içerisinde elementi bulup tıklayıp kullanıcı adı ve şifreyi ilgili kutuya gönderen aksiyon zincirini oluşturdum ve perform ettim. Ardından Ürünleri sepete ekleme butonunu bularak tıklattım ve açılan sayfada ürünün olup olmadığını assertledim. Tabi screenshot almayı da unutmadım.

## test_image_ctrl fonksiyonu

Bu fonksiyonun başında decorator'lerden biri olan @pytest.mark.xfai'i kullandım. Çünkü bu testin false geleceğini biliyorum ve testte hata almak istemiyorum. Setup işlemlerinin ardından diğer fonksiyonlardaki gibi username kısmını bulup tıklatıp kullanıcı adını gönderen bir aksiyon zinciri oluşturdum ve perform ettim ardından password kısmı için de aynı şeyi yaptım. Şimdi eğlenceli yere geliyoruz :) entry_images adında girişteki resimleri buldum ardından entry_images_url_list adında boş bir liste oluşturdum ve for döngüsü yardımıyla girişteki her resme get_attribute("src") kullanarak her resmin url'ini alıp append ile url_liste ekledim. Ardından num_of_img adındaki değişkene len() kullanarak ürün sayısını değişkene atadım ve döngüyü bitirdim. Sonrasında  boş bir second_images_url_list oluşturdum. Bir for döngüsü oluşturdum bu for döngüsü ürün listesindeki ürün adedi kere çalışacak ve içerisinde entry_images ile bulduğumuz elementlere index sırasıyla tıklayacak tıkladığı elementten yeni açılan sayfada classname ile yeni resmi bulacak ve get_attribute ile url'ini alacak son olarakiseappend ile second_images_url_list'e ekleyecek. Ardından screenshot'ı alıp son bir for döngüsüyle entry_images_url_list ve second_images_url_list'i index yardımıyla elemanlarını assertledim. Bu işlemi problem user kullanıcısıyla yaptım ilk resimler farklı ve (1'i hariç) ikinci resimler farklıydı. Assert'le de assert not'la da hata alacağım için xfail decorator'ünü kullandım.

## test_different_user fonksiyonu

Setup işlemlerinin ardından username kısmını buldurup tıklatıp problem_user kullanıcı adını yazdırdıktan sonra password işlemi için de şifreyi yazarak bilgileri yazıyorum. sonrasında login butonu bulup tıklıyorum. Giriş yaptıktan sonra bir ürünü sepete ekleyip logout butonunu buldurup tıklıyorum ve çıkış yapıyorum. Sonrasında giriş yapmak için aynı adımları izliyorum fakat bu sefer farklı bir kullanıcı olan standard_user kullanıcı adıyla giriş yapıyorum. Sonrasında sepeti buldurup tıkltaıyorum. Farklı bir kullanıcı girişi olması sebebiyle sepetin boş olmasını ve farklı birhesapta eklediğim ürünün burada bulunmaması gerektiğini düşünerek ürünün locator'ı ile ürünü burada assert not'lıyorum. Bu kısım sitede doğru çalışmıyor ve eklenilen ürün farklı kullanıcıda da gözüküyor bu sebeple testin sonucu fail olacağından xfail decorator'ünü kullanıyorum.

## test_product_num_in_basket fonksiyonu

Setup fonksiyonundaki işlemlerin ardından username kısmını buldurup tıklatıp kullanıcı adını göndermeyi perform ediyorum sonrasında password kısmı için de password kısmını bulup tıklatıp şifreyi göndermeyi perform ediyorum. add_cart_buttons adında bir değişken oluşturarak ve find_elementsi kullanarak sayfadaki sepete ekleme butonlarını buluyorum. sonrasında random_num adında bir değişken oluşturup 1 ve 6 aralığında randint kullanıp int() ile döngüde kullanabilir hale getiriyorum. Döngümü oluşturmadan önce de index adında bir değişken oluşturup 0'a eşitliyorum. For döngümde random_num adındaki değişkenimi kullanarak o an rastgele seçilen sayı kadar döngümün çalışmasını istiyorum. add_cart_buttons'ı burada tekrar bulduruyorum ce index değişkenimi index kısmına yazarak click ettiriyorum. webdriverwait ile 2 saniye uyutmanın ardından indexi bir arttırıp döngüye devam ediyorum. Alışveriş sepetinin üzerindeki rakam bulunan yuvarlak kısmı locator ile buldurarak .text ile içerisindeki rakamı alıyorum ve int halinde bulunan random_num değişkenimi str() işleminden geçirerek bu iki rakamı assert'lüyorum. Parametrize decorator'ü ile kullanıcıad ve şifresini 4 farklı ikiliyle denetiyorum ve fail alacak ikilileri pytest.param ve marks=pytest.mark.xfail ile bu faillerden kurtuluyorum. Denenecek parametreler arada doğru sonuçlar verse de çoğunlukla assert'e uymadığı için xfail ile garantiye almak istedim.


## test_total_price_ctrl fonksiyonu

Setup işlemlerinin ardından username kısmını buldurup tıklattırıp kullanıcı adını gönderen bir aksiyon zinciri oluşturuyorum. Bunu password kısmı için de yapıyorum ve ikisini de perform edip login butonuna tıklattırıyorum. Sonra add_cart_buttons adında bir değişken oluşturup ürünü sepete ekleme butonlarunu buluyorum ve prices adında bir değişken oluşturup ürünlerin fiyatlarını içeren elementleri buluyorum. price_list adında boş bir liste oluşturuyorum ve sonrasında prices değişkeninin içerisinde gezebilmek in bir for döngüsü oluşturuyorum bu döngünün içinde her bir ürün fiyat elementindeki text'i alıp fiyat dışındaki dolar işareti ve boşlukları siliyorum ve kalanı prie_list'e ekliyorum. Böylelikle elimde sadece fiyatların bulunduğu liste oluyor. Sonrasında add_cart_buttons_list adında bir boş liste oluşturup for döngüsüyle buttonları append kullanarak add cart buttons listesine  ekliyorum. Sonrasında dict(zip())kullanarak buton ve fiyat listelerinden bir kütüphane oluşturuyorum. Sonrasında random_num adında, random.randint() kullanarak 1 ve 6 arasında rastgele sayı alan bir değişken oluşturdum. Bu değişkeni döngüiçerisinde kullanabilmek için int() yapısını kullandım. index değişkeni oluşturup 0'a eşitledim. total_value değişkeni oluşturup 0'a eşitledim. for  döngüsü oluşturup random_num kadar çalışmasını istedim. Döngü içerisindeise Önce add_cart_button_listteli ilk index'e tıklattım sonrasında price_list'teki ilk fiyato float'layarak total_value'ye topla eşitle yaptım. döngünün sonunda ise index'i 1 arttırarak döngüyü devam ettirdim. Döngüden çıktıtan sonra alışveriş sepeti görselini buldurarak tıklattım sonrasında checkout butonunu buldurup tıklattım. Ekranda ad soyad ve posta kodu isteyen kutucuklar içiin her birine ayrı olacak şekilde buldurup tıklatıp bilgi göndererek performettim.Ardından devam etme butonunu bulup tıklattırdıktan sonra toplam fiyatın bulunduğu elementi buldurdum. Sonrasında Benim topladığım fiyatlar dışında vergiler de eklendiği için vergi kısmını da farklı bir değişkende buldurdum. Vergi kısmındaki tax stringi, dolar işareti ve boşluğu da .text ve replace'i kullanarak sildim ve vergiyi float'ladım. Hem ürünlerin hem verginin toplamı olan sondaki fiyatın da bana gerekli olmayan yerlerini silebilmek için .text ve replace'i kullanarak fiyat float'u dışındaki her yeri sildim. tax_plus_value adında for döngümden aldığım toplam fiyat ile vergiyi toplayarak elde ettiğim bir değişken oluşturdum.
Toplam fiyatı hesaplarken virgülden sonra sadece 2 rakamı aldıkları için bu değişkenin de virgülden sonra sadece 2 rakamını alabilmek için round(x,2) yapısını kullandım.
Screenshot'ımı aldıkran sonra tax_plus_value ve items_total_on_last_page değişkenlerini assertledim.






































