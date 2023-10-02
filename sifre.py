import random

karaktersayisi = int(input("kaç karakterli bir şifre istersiniz?"))

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifre = []
for i in range(karaktersayisi):
    x= random.choice(karakterler)
    sifre.append(x)

print(sifre)
