class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{amount} TL yatırıldı. Yeni bakiye: {self.balance} TL"
        else:
            return "Geçersiz işlem."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"{amount} TL çekildi. Yeni bakiye: {self.balance} TL"
        else:
            return "Yetersiz bakiye veya geçersiz işlem."

def main():
    atm = ATM()

    while True:
        print("1 - Bakiye Sorgula")
        print("2 - Para Yatır")
        print("3 - Para Çek")
        print("4 - Çıkış")
        
        choice = int(input("Lütfen yapmak istediğiniz işlemi seçin: "))

        if choice == 1:
            print("Bakiye:", atm.check_balance())
        elif choice == 2:
            amount = float(input("Yatırmak istediğiniz tutarı girin: "))
            print(atm.deposit(amount))
        elif choice == 3:
            amount = float(input("Çekmek istediğiniz tutarı girin: "))
            print(atm.withdraw(amount))
        elif choice == 4:
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()