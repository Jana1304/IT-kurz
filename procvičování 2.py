#součet dvou čísel 
cislo_1 = int(input("Zadej první číslo: "))
cislo_2 = int(input("Zadej druhé číslo: "))
vysledek = (cislo_1 + cislo_2)
print("Výsledek je: ", vysledek)

#součet, součin a rozdíl
a = float(input("Napiš první číslo: "))
b = float(input("Napiš druhé číslo: "))
součet = a + b
součin = a * b 
rozdíl = součet - součin
print("Součin tvých čísel je: ", součin)
print("Součet tvých čísel je: ", součet)
print("Rozdíl mezi součtem a součinem je: ", rozdíl)

#zbytek po dělení 
cislo_3 = float(input("Zadej první číslo: "))
cislo_4 = float(input("Zadej druhé číslo: "))
vysledek_1 = round((cislo_3 % cislo_4), 2)

#umocňování 
cislo_5 = int(input("Zadej číslo: "))
vysledek_2 = (cislo_5 ** 2)
vysledek_3 = (cislo_5 ** 3)
print("Druhá mocnina tvého čísla je, ", vysledek_2, "a třetí mocnina je, ", vysledek_3)
