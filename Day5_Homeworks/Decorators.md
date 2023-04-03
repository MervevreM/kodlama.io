# Decorators

## @pytsest.mark.xfail()
Sonucunun false dönmesini beklediğimiz fonksiyonlarda kullanılır.

    import pytest 
    @pytest.mark.xfail()
    def control():
      assert 2 == 3

## @pytest.mark.parametrize()
Aynı fonksiyonu birden fazla farklı parametreyle çalıştırmak istediğimizde kullanabileceğimiz bir decoratordür. 
           
          @pytest.mark.parametrize(50,2,(10,5),(96,6),(8,4)])
           def tam_bol(50,2):
              sonuc = 50 ½ 2 
              assert sonuc == 0

Girdiğimiz farklı parametrelere göre false dönmesini beklediğimiz senaryolar için xfail decoratorüyle entegre edilebilmektedir.
          
          @pytest.mark.parametrize(50,2,(10,5),
              (96,6),
              (8,4),
              pytest.param(191,10,marks=pytest.mark.xfail)
              ])
           def tam_bol(50,2):
              sonuc = 50 ½ 2 
              assert sonuc == 0
      
      
 ## @pytest.mark.skip()
Çalıştırmak istemediğimiz fonksiyonlarda kullanılabilen bir decoratordür. Üzerine yazıldığı fonksiyonu atlar.
        
        @pytest.mark.skip():
        def tamamlanmamis_fonksiyon():
            for i in range(15):
                total = 0
                toplam +
              
              
## @pytest.mark.skipif()
Belirlediğimiz koşul sağlanırsa fonksiyonu atlayan bir decoratordür.
  
      
        @pytest.mark.skipif(value >15000, reason= "pc is gonna tired")
        def math(value):
            value = input("gie me a nnumber: ")
            value = int(value)
            power = value*value
            power2 = value**2
            assert power == power2
        
        