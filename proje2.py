import smtplib
import time

# E-posta gönderen hesap bilgileri
sender_email = 'your_sender_email@gmail.com'
sender_password = 'your_sender_password'

# E-posta alıcıları
recipient_emails = ['recipient1@example.com', 'recipient2@example.com']

# Eşik değeri
threshold = 0.5

def send_email(subject, body):
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            for recipient_email in recipient_emails:
                message = f"Subject: {subject}\n\n{body}"
                server.sendmail(sender_email, recipient_email, message)

            print("E-posta gönderildi.")
    except Exception as e:
        print(f"E-posta gönderirken hata oluştu: {e}")

# MQ-2 sensöründen veri okuma fonksiyonu (simüle edilmiş veri)
def read_sensor():
    # Simüle edilmiş sensör değeri
    return 0.7 if input("Duman algılandı mı? (e/h): ").lower() == 'e' else 0.3

# Ana program
if __name__ == "__main__":
    while True:
        sensor_value = read_sensor()

        if sensor_value > threshold:
            email_subject = "Sigara Dumanı Algılandı!"
            email_body = f"MQ-2 sensörü tarafından sigara dumanı veya kokusu algılandı! Sensör değeri: {sensor_value}"
            send_email(email_subject, email_body)

        # Belirli bir süre bekleyerek tekrar kontrol et
        time.sleep(60)  # Örneğin, her 1 dakikada bir kontrol