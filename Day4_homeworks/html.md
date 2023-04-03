# HTML 

Sanılanın aksine bir programlama dili değilmiş (Ben de yeni öğrendim.). HTML web sayfasındaki görüntüyü oluşturmak için yazılır. Web sayfasının iskeletini oluşturur. Görselin konumu, yazının boyutu yeri gibi görsel ögeleri konumlandırır ve şekillendirir. Oldukça basit olmasının yanında Web sayfası oluşturmak isteyen herkesin bilmesi gereken bir dildir. 

## HTML locaters 

Locater İngilizce konumlandırıcı anlamına gelmektedir. Anlamından da anlaşılacağı üzere ögelerin konumlarını belirlemekte kullanılırlar. Üzerinde çalışmakta olduğumuz Selenium için locater'lar  oldukça önemlidir. İşlem ve kontrol yapmak istediğimiz ögenin yerini bulmak ve sürecin doğru işlediğinden emin olmamız gerekir. Ögelerin yerini Selenium'a belirtebilmek find_element(By.)metodunu kullanmamız gerekir ve bu metodun içinde kullanacağımız bize yol gösterecek bir çok locater vardır. Bunlar : "Id, Name, Class Name, TagName, LinkText, CssSelector, XPath". Ögeyi bulmak için önceliğimiz id olmalıdır. Sebebi  ise id'nin sayfalarda tek, eşsiz olmasıdır. 

## Selenium'da  en sık kullanılan action'lar;

find_element() = ögenin adresini içine yazarak ögenin yerini bulmamızı sağlar.

click() = Yeri verilip tanımlanmış olan ögeye tıklar.

double_click() =Yeri verilip tanımlanmış olan ögeye çift tıklar.

send_keys() = İçerisine yazılanları yeri belirlenmiş ögeye gönderir.
