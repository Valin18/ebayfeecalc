import os
import sys

def clear():
    """
        Bu fonksiyon terminal penceresini ilk haline getirir.
    """
    # İşletim Sistemi Windows ise
    if os.name == 'nt':
        _ = os.system('cls')
    # İşletim Sistemi MacOS ise
    elif os.name == 'mac':
        _ = os.system('clear')
    # İşletim Sistemi Linux ise
    elif os.name == 'posix':
        _ = os.system('clear')
    # Yabancı bir işletim sistemi ise
    else:
        _ = os.system('clear')


equal = 0.0
tax = 8
sell_price = 0.0
take_price = 0.0
f_v_fee = 0.0
ı_fee = 0.0
fee_equal = 0.0
vat = 0.0
promote_price = 0.0
fee_promote_equal = 0.0


sell_price = float(input("Satış Fiyatınızı Giriniz: "))
take_price = float(input("Alış Fiyatınızı Giriniz: "))
promote_price = float(input("Reklam Fiyatını Girin: "))

equal = sell_price + tax
f_v_fee = equal * 12.9 / 100
ı_fee = equal * 1.55 / 100
fee_equal = f_v_fee + ı_fee + 0.30
vat = fee_equal * 18 / 100
fee_equal = fee_equal + vat
fee_promote_equal = promote_price + fee_equal

clear()

print("Satış Fiyatı: " + str(sell_price) + " Alış Fiyatı: " + str(take_price) + " Reklam Fiyatı: " + str(promote_price) + "\n\n(Reklam Dahil Değil) Alınan Fee Değeri: " + str(round(fee_equal, 2)) + "\n\n(Reklam Dahil) Alınan Fee Değeri: " + str(round(fee_promote_equal, 2)))
sell_price = sell_price - fee_equal
print("\nSatıştan sonra size kalacak miktar: " + str(round(sell_price, 2)))
sell_price = sell_price - take_price
print("\nSatıştan edilecek ortalama net kâr: " + str(round(sell_price, 2)) + "\n")

