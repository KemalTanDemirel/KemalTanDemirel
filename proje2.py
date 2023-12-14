import machine
import utime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# AO (Analog Output) pinini GP26'ya bağlayın
analog_pin = 26

adc = machine.ADC(0)  # ADC nesnesini oluşturun (GP26'ya bağlı)
threshold = 500  # Eşik değeri

def send_email(sensor_value):
    sender_email = "your_email@gmail.com"
    sender_password = "your_email_password"
    recipient_email = "recipient_email@example.com"

    # E-posta başlığı ve içeriği
    subject = "MQ-2 Sensor Alarm"
    body = f"MQ-2 sensor detected high value: {sensor_value}"

    # E-posta oluştur
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # SMTP sunucusuna bağlan
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # E-posta gönder
        server.sendmail(sender_email, recipient_email, msg.as_string())

def main():
    while True:
        sensor_value = adc.read_u16()

        # Okunan veriyi eşik değeri ile karşılaştırın
        if sensor_value > threshold:
            print(f"MQ-2 sensöründen yüksek değer algılandı: {sensor_value}")
            send_email(sensor_value)

        # Belirli bir süre bekle
        utime.sleep(5)  # Örneğin, her 5 saniyede bir kontrol

if __name__ == "__main__":
    main()