veta = "zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu"
samohlasky = "aeiouáéíóú"
souhlasky = "bcčdďfghjklmnňprřsštťvzžcdž"
vysledek = {"souhlasky": 0, "samohlasky": 0}

for pismeno in veta:
    if not pismeno.isalpha():
        continue
    elif pismeno.lower() in samohlasky:
        vysledek["samohlasky"] += 1
    elif pismeno.lower() in souhlasky:
        vysledek["souhlasky"] += 1
print("Počet souhlásek: ", vysledek["souhlasky"], "| Počet samohlásek: ", vysledek["samohlasky"])

cisla = [1, 2, 3, 4, 5, 6, 7, 8]
suda = 0
licha = 0

for cislo in cisla:
    if cislo % 2 == 0:
        suda = suda + cislo
    else:
        licha = licha + cislo
vysledek = abs(suda - licha)
print("Rozdíl je: ", vysledek)

seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]
delky_slov = {slovo: len(slovo) for slovo in seznam_slov}
print(delky_slov)