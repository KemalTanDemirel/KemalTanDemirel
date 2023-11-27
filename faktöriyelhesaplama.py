def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n-1)

sayi = int(input("Faktöriyeli hesaplanacak sayıyı girin: "))
result = faktoriyel(sayi)
print(f"{sayi}! = {result}").                     farkli bir örnek:                                 def faktoriyel_hesapla(sayi):
    if sayi == 0 or sayi == 1:
        return 1
    else:
        return sayi * faktoriyel_hesapla(sayi - 1)

try:
    kullanici_sayi = int(input("Faktöriyeli hesaplanacak bir sayı girin: "))
    if kullanici_sayi < 0:
        print("Negatif sayıların faktöriyeli hesaplanamaz.")
    else:
        faktoriyel_sonuc = faktoriyel_hesapla(kullanici_sayi)
        print(f"{kullanici_sayi}! = {faktoriyel_sonuc}")
except ValueError:
    print("Geçersiz giriş. Lütfen bir tam sayı girin.")