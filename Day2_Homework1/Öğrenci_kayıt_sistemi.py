############################################ ÖĞRENCİ SİSTEMİ ###################################

print ("Öğrenci kayıt sistemine hoşgeldiniz")

Students = []

islemler = ["öğrenci eklemek", "öğrenci silmek", "Öğrenci listesini görmek", "Öğrencinin numarasını öğrenmek"]
for numara, islem in enumerate(islemler,1):
    print(f"{islem} için tuşlamanız gereken rakam : {numara}.")


def Öğrenci_iste():
    isim = input("Öğrencinin ismini giriniz: ")
    soyisim = input("Öğrencinin soyismini giriniz: ")
    isim_ikilisi = isim + ' ' + soyisim
    return isim_ikilisi


def ogrenci_kayit():
    isim_ikilisi = Öğrenci_iste()
    if isim_ikilisi in Students:
        print(f"{isim_ikilisi} listeye önceden eklenmiş.")
    else:
        Students.append(isim_ikilisi)
        print(f"{isim_ikilisi} sisteme basariyla kaydedildi.")
        return Students
        





def ogrenci_silme():
    while True:
        isim_ikilisi = Öğrenci_iste()
        if isim_ikilisi in Students:
            Students.remove(isim_ikilisi)
            print("Öğrenci silindi")
            break
        else:
          print(f"{isim_ikilisi} listede yok")
          break
            

          

while True: 
    while True:
        istenen_islem = input("Yapmak istediğiniz isleme ait rakami tuslayiniz: ")
        if istenen_islem.isdigit():
            if int(istenen_islem) == 1:
                ogrenci_kayit()
                break
            if int(istenen_islem) == 2:
                ogrenci_silme()
                break
            if int(istenen_islem) == 3:
                print(Students)
                break
            if int(istenen_islem) == 4:
                isim_ikilisi = Öğrenci_iste()
                print(Students.index(isim_ikilisi))
            else:
                print("Girdiğiniz rakama ait bir işlem bulunmamaktadir.")
        else:
            print("Lütfen işleme ait RAKAM girişi yapin.")