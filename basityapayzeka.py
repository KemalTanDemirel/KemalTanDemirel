import random

def basit_yapay_zeka(cevaplar, soru):
    cevap = cevaplar.get(soru.lower(), "Ne anlatiyon amk?")
    return cevap

if __name__ == "__main__":
    cevaplar = {
        "nasılsın": "kötüyüm sen nasılsın?",
        "adın ne": "yapay zeka",
        "ne yapıyorsun": "seni.",
        # İstediğiniz kadar soru ve cevap ekleyebilirsiniz.
    }

    print("Merhaba! Sorularınızı bana sorabilirsiniz. Çıkmak için 'çık' yazabilirsiniz.")

    while True:
        soru = input("Soru: ")
        
        if soru.lower() == 'çık':
            print("siktir git!")
            break

        cevap = basit_yapay_zeka(cevaplar, soru)
        print("Cevap:", cevap)