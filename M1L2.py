import random

karakterler = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("Şifren'in uzunluğu ne kadardır ?"))

parola = ""

for i in range(uzunluk):

    parola += random.choice(karakterler)

print("Oluşturulan şifre:", parola)