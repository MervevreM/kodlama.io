# Öğrenci Kayıt sistemindeki fonksiyonların açıklaması

## Öğrenci_iste fonksiyonu
2 ayrı inputla öğrenci adı ve soyadını alarak isim_ikilisi isimli değişkende boşlukla birlikte birleştirdim ve diğer fonksiyonlar içerisinde kullanabilmek için return ettim.

## Öğrenci_kayit fonksiyonu
Bu fonksiyonda öğrenci_iste fonksiyonunu çağırarak return ettiğim isim_ikilisinin öğrenci listesinde olup olmadığını if ile test ettim. Eğer varsa kullanıcıya "Bu öğrenci zaten var" uyarısında bulundum. Ad soyadı verilen öğreni yok ise listeye ekledim. Students adını verip en başta boş liste olarak tanımladığım listeyi burada returnleyip ileride kullanmak istediiğim yerlerde öğrenci ekli şekilde kullanabilmek için returnledim. (Bu çok kullanışlı olmadı biliyorum. Her yeni çalıştırışta liste sıfırlanacak çünkü.)

## Öğrenci_silme fonksiyonu
Bu fonksiyonda da öğrenci isteme fonksiyonunu çağırarak kullanıcıdan silmek istedikleri öğrenciin isim ve soyisimini istedim. Aldığım ad soyadı öğrenci listesinde "is in" ile aratarak girilen isim soyisim listede varsa sildim yoksa kullanıcıya "Bu öğrenci zaten kayıtlı değil" uyarısında bulundum. 

## while döngüsü
Fonksiyonlarımı tanımladıktan sonra kullanıcıdan yapmak istedikleri işlemi daha hızlı seçebilmeleri için her fonksiyonu numaralandırdım. Ayrıca öğrenci listesini görebilecekleri bir seçenek ve her öğrencinin liste indexinin öğrenci numarası varsayarak, öğrenci numarasına isim ve soyisim ile erişilebilecek bir seçenek ekledim. Ekstra olarak işlem numarasını girecek olan kullanıcının işlemini kontrol etmek ve hata almamak adına kullanıcının rakam girdiğine emin olduğum bir adım ve girilen rakama ait bir fonksiyonun olduğundan emin olduğum bir adım ekleyerek kullanıcı uygun bir rakam girene kadar kullanıcıyı döngüye sokarak bir işlem gerçekleştirdikten sonra döngüden çıkmasını sağladım.
