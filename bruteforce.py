import os
import time
import subprocess
from termcolor import colored

def install_requirements():
    if not os.path.exists("requirements_installed.txt"):
        print(colored("Kurulum başlıyor...", "yellow"))
        time.sleep(1)
        os.system("pkg install python -y")  # Python kurulumu
        os.system("pip install termcolor")  # Termcolor kurulumu
        with open("requirements_installed.txt", "w") as f:
            f.write("Kurulum tamamlandı.")

def display_menu():
    os.system("clear")  # Menüyü her seferinde temizle
    print(colored("--- CREATEXSW ---", "cyan", attrs=['bold']))
    print(colored("1. Brute Force Araçları", "green"))
    print(colored("00. Doğru Şifreleri Göster", "blue"))
    print(colored("99. Çıkış", "red"))

def brute_force(username, wordlist):
    print(colored(f"Brute force işlemi {username} için başlatıldı...", "yellow"))
    with open(wordlist, 'r') as file:
        for password in file:
            password = password.strip()
            print(colored(f"Deniyor: {password}", "yellow"))
            # Burada doğru şifre kontrolü yapılmalıdır
            if password == "dogruSifre":  # Buraya doğru şifre kontrol mekanizmasını ekle
                with open("dogru.txt", "a") as correct_file:
                    correct_file.write(f"{username}:{password}\n")
                print(colored(f"Doğru şifre bulundu: {password}", "green"))
                break
            else:
                print(colored(f"Yanlış şifre: {password}", "red"))
            time.sleep(0.5)  # Her deneme arasında kısa bir bekleme süresi ekle

def show_correct_passwords():
    os.system("clear")  # Doğru şifreleri gösterirken ekranı temizle
    if os.path.exists("dogru.txt"):
        print(colored("Doğru Şifreler:", "magenta"))
        with open("dogru.txt", 'r') as file:
            for line in file:
                print(colored(line.strip(), "green"))
    else:
        print(colored("Doğru şifre kaydı bulunamadı.", "red"))

def main():
    install_requirements()
    
    while True:
        display_menu()
        choice = input(colored("Seçiminizi yapın: ", "cyan"))

        if choice == "1":
            username = input(colored("Kullanıcı adını girin: ", "cyan"))
            wordlist = input(colored("Wordlist dosyasının yolunu girin: ", "cyan"))
            brute_force(username, wordlist)

        elif choice == "00":
            show_correct_passwords()
            input(colored("Devam etmek için bir tuşa basın...", "cyan"))  # Kullanıcıdan bir tuşa basmasını iste

        elif choice == "99":
            print(colored("Çıkış yapılıyor...", "red"))
            subprocess.run(["termux-open-url", "https://youtube.com/@createxsw"])
            break

        else:
            print(colored("Geçersiz seçim, lütfen tekrar deneyin.", "red"))

if __name__ == "__main__":
    main()
