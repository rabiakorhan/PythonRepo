while True:
    Sayi1 = float(input("Birinci sayıyı giriniz: "))
    Sayi2 = float(input("İkinci sayıyı giriniz: "))
    islem = input("Yapmak istediğiniz işlemi yazınız. (toplama, çıkarma, çarpma, bölme): ")

    if islem == "toplama":
        print("İşlem sonucunuz: ", Sayi1 + Sayi2)
    elif islem == "çıkarma":
        print("İşlem sonucunuz: ", Sayi1 - Sayi2)
    elif islem == "çarpma":
        print("İşlem sonucunuz: ", Sayi1 * Sayi2)
    elif islem == "bölme":
        if Sayi2 != 0:
            print("İşlem sonucunuz: ", Sayi1 / Sayi2)
        else:
            print("0'a bölme hatası.")
    else:
        print("Geçersiz işlem türü. Lütfen toplama, çıkarma, çarpma veya bölme giriniz.")

    devam = input("Başka bir işlem yapmak istiyor musunuz? (evet/hayır): ")
    if devam != "evet":
        print("Programdan çıkılıyor.")
        break
