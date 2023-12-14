import machine
import utime

# AO (Analog Output) pinini GP26'ya bağlayın
analog_pin = 26

adc = machine.ADC(0)  # ADC nesnesini oluşturun (GP26'ya bağlı)
threshold = 500  # Eşik değeri

while True:
    sensor_value = adc.read_u16()

    # Okunan veriyi eşik değeri ile karşılaştırın
    if sensor_value > threshold:
        print(f"MQ-2 sensöründen yüksek değer algılandı: {sensor_value}")

    # Belirli bir süre bekle
    utime.sleep(1)