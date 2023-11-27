import math

def hesap_makinesi():
    print("Hesap Makinesi Programına Hoş Geldiniz!")
    while True:
        try:
            sayi1 = float(input("İlk sayıyı girin: "))
            operator = input("İşlemi seçin (+, -, *, /, sqrt, pow): ")

            if operator.lower() == "sqrt":
                sonuc = math.sqrt(sayi1)
            elif operator.lower() == "pow":
                us = float(input("Üs değerini girin: "))
                sonuc = math.pow(sayi1, us)
            else:
                sayi2 = float(input("İkinci sayıyı girin: "))

                if operator == "+":
                    sonuc = sayi1 + sayi2
                elif operator == "-":
                    sonuc = sayi1 - sayi2
                elif operator == "*":
                    sonuc = sayi1 * sayi2
                elif operator == "/":
                    if sayi2 != 0:
                        sonuc = sayi1 / sayi2
                    else:
                        print("Hata! Sıfıra bölme hatası.")
                        continue
                else:
                    print("Geçersiz operatör. Lütfen geçerli bir operatör seçin.")
                    continue

            print(f"Sonuç: {sonuc}")

            devam_et = input("Başka bir hesaplama yapmak istiyor musunuz? (Evet/Hayır): ")
            if devam_et.lower() != "evet":
                print("Hesap makinesi kapatılıyor. İyi günler!")
                break

        except ValueError:
            print("Hata! Geçerli bir sayı girin.")
        except Exception as ex:
            print(f"Hata oluştu: {ex}")

hesap_makinesi()