# Projekt generatora haseł pseudo - losowych
import random
znaki = "qwertyuioplkskrtyudhternmbzvxcjseySEWACRTGYDSSZVNKOUGBFRTUIOPLMN<,.>:;?/|1234567890!@#$%^&*())_-+="
ile_hasel = 0
while ile_hasel <= 0:
    try:
        ile_hasel = int(input("Witaj w programie. Podaj ile chcesz haseł: "))
    except:
        print("Niestety wpisano błędny znak !!!")

dlugosc = 0
while (dlugosc <= 5 or dlugosc >= 65 ):
    try:
        dlugosc = int(input("Podaj długość haseł ( 6-64): "))
    except:
        print("Niestety wpisano błędny znak !!!")\

for i in range(ile_hasel):
    haslo =[]
    for j in range(dlugosc):
        index = random.randint(0,len(znaki)-1)
        haslo.append(znaki[index])
    print("".join(haslo))
