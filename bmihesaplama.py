def bmi_hesapla(kilo, boy_cm):
    try:
        kilo = float(kilo)
        boy_m = float(boy_cm) / 100  # Santimetre cinsinden boyu metreye çevir
        bmi = kilo / (boy_m ** 2)
        return bmi
    except ValueError:
        return "Lütfen geçerli sayısal değerler girin."

kilo = input("Kilonuzu kilogram cinsinden girin: ")
boy_cm = input("Boyunuzu santimetre cinsinden girin: ")

sonuc = bmi_hesapla(kilo, boy_cm)

if type(sonuc) == float:
    print(f"Vücut Kitle Endeksiniz: {sonuc:.2f}")
else:
    print(sonuc)