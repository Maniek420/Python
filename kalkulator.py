#variables

pytanie = "Co chcesz policzyć?"
pytanieL = "Podaj liczbę - "
pytanieZ = "Podaj znak - "

#code

print(pytanie)
liczba1 = input(pytanieL)
znak = input(pytanieZ)
liczba2 = input(pytanieL)

if znak == "+":
    sum = int(liczba1) + int(liczba2)

if znak == "-":
    sum = int(liczba1) - int(liczba2)

if znak == "*":
    sum = int(liczba1) * int(liczba2)

if znak == "/":
    sum = int(liczba1) / int(liczba2)

if znak == "%":
    sum = int(liczba1) % int(liczba2)

print("Wynik to",sum)
