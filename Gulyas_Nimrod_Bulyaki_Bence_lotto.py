
import random

valasz = input("A szerencsejáték függőséget okoz! Biztos szeretnél játszani?(i/n): ")
if valasz == ("i"):
    print("Add meg a lottószámokat!")


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


# for num in range (5):
#     sorsoltszamok = random.randint(1,91)
#     lottoszamok.append(sorsoltszamok)

lottoszamok = []

for num in range (5):
    sorsoltszamok = random.randint(1,91)
    lottoszamok.append(sorsoltszamok)

print(f'A  gép által sorsolt számok: {lottoszamok}')



talalatok = []
vegso = []
vegso.append(len(set(lottoszamok) & set(szamok)))
talalatok_szama = (len(set(lottoszamok) & set(szamok)))
print(f"A találataid száma: {talalatok_szama}!")


if 1 in vegso:
    print('Nyertél 500 Ft- ot!')
elif 2 in vegso:
    print('Nyertél ezer öccá forintot!')

elif 3 in vegso:
    print("Nyertél 100k forintot!")

elif 4 in vegso:
    print("Nyertél 5 millió forintot!")

elif 5 in vegso:
    print("Halooooooo 5-ös lottód van he megnyerted a szerelmem!")

else:
    print("Sajnos nem nyertél!")

# for szam in szamok:
#     if szam in lottoszamok:
#         talalatok.append(szam)
# print(talalatok)

