"""
2-3 fős csoportokban készítsetek egy lottó játékot!
Legyen lehetőség a játékos tippjeinek a felvételére!
Utána a program sorsoljon ki számokat!
Végül írjuk ki, hogy mennyi találat volt!
Ha tudjátok, többféle lottó játékkal is lehessen játszani!
"""

import random

szamok = []
for i in range (5):
    while True:
        try:
            szam = int(input(f'{i+1}. szám: '))
            szamok.append(szam)
            break
        except ValueError as e:
            print(e)
            print("Nem számot adtál meg!")
    if szam > 90 and szam < 1:
        print("1-90-ig tudsz számokat megadni!")
        break
print(f'A megadott számaid: {szamok}')

lottoszamok = []

for num in range (5):
    sorsoltszamok = random.randint(1,91)
    lottoszamok.append(sorsoltszamok)

print(lottoszamok)

