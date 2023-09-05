"""
----FONKSIYON----

def myfunc(a):
    print(a)

myfunc('Deli')

def addList(**args):
    for a in args.items:
        list().append(a)
        print (list)

addList('Ali', 'Ata', 2, 'Defa', 'Bak')
"""

"""
def asalSayiBul(a, b):
    asalSayilar = []
    if a < b:
        for i in range(a, b + 1):
            is_asal = True  # Bu değişken, i'nin asal olup olmadığını belirtir
            for x in range(2, i):  # 2'den i'ye kadar olan sayılarla kontrol ediyoruz
                if i % x == 0:
                    is_asal = False  # Eğer i, x'e tam bölünüyorsa asal değil
                    break
            if is_asal:
                asalSayilar.append(i)
        return asalSayilar
    else:
        return None 
    
print(asalSayiBul(7,50))
    
"""

"""
def bolermi(a):
    bolenler = []
    for i in range(2, a+1):
        if a % i == 0:
            bolenler.append(i)
    return bolenler  

print(bolermi(30))
"""
"""

----OOP----

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
"""

'''
----HATA YONETIMI----

while True:
        try:
            x = int(input('x: ') )
            y = int(input('y: '))
            print(x/y)
        except Exception as ex:
            print('yanlis bilgi girdiniz', ex)
        else:
            break
        finally:
            print('try except sonland1.')
'''

'''           
def faktoriyel(x):
    x = int(x)
    if x <0:
         raise ValueError('Negatif deger')
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

for x in [5, 10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
'''

'''
----DECORATOR----

import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time. sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print("fonksiyon"+" "+func.__name__+" "+str(finish-start) +" "+"saniye sürdü.")
    return inner 

@calculate_time
def usalma(a,b):
    print (math. pow (a, b))

usalma(2,3)
'''

'''
----ITERATORS----

class MyNumbers:
    def __init__ (self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

list = MyNumbers(10,20)

for x in list:
    print(x)

myIter = iter(list)

print(next(myIter))
'''


