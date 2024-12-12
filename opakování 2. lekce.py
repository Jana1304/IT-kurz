#zadaný seznam
zamestnanci = ["František", "Bruno",
               "Anna", "Jakub",
               "Klára", "Anežka",
               "Anežka", "Anežka"]
#zjisti poslední index
posledni_index = len(zamestnanci) - 1
#hodnota na druhém indexu
print("Na indexu 2 je: ", zamestnanci[2])
#jmeno na posledním indexu
print("Na", posledni_index, "indexu je:", zamestnanci[posledni_index])
#jména od indexu 2 do 5
print("V intervalu od 2 do 5 je:", zamestnanci[2:6])
#každý třetí údaj
print("Každý třetí člen je:", zamestnanci[::3])


#bmi
jmeno = "Martin"
vaha_v_kg = 80
vyska_v_m = 2
bmi = vaha_v_kg / vyska_v_m **2
if bmi > 40:
    kategorie = "težká obezita"
elif bmi > 30:
    kategorie = "obezita"
elif bmi > 25:
    kategorie = "mírná nadváha"
elif bmi > 18.5:
    kategorie = "zdravá váha"
else:
    kategorie = "podvýživa"
print(jmeno, "tvé bmi je", bmi, "což spadá do kategorie", kategorie, ".")

#vytvoř list zaměstnanci
zaměstnanci = ["František", "Anna", "Jakub", "Klára"]
#vypiš obsah
print("Zaměstanci na začátku: ", zaměstnanci)
#zkopírovaný list
zaměstnanci_a = zaměstnanci.copy()
#přidání jmen
zaměstnanci_a.append("Bruno")
zaměstnanci_a.append("Anežka")
#vypsání nový seznam
print("Nová jména přidána: ", zaměstnanci_a)
#druhá kopie
zaměstnanci_b = zaměstnanci.copy()
#index 1
zaměstnanci_b.insert(1, "Bruno")
#obsah proměnné zamestnanci_b
print("Nová jména vložena: ", zaměstnanci_b)

#proměnné 
vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')
cislo_dne = 3
den_tydne = tyden[cislo_dne - 1]
#je cislo dne v listu vstupni cisla
if cislo_dne in vstupni_cisla:
    print("Správná vstupní hodnota!")
    if den_tydne.startswith(vstupni_pismena[cislo_dne - 1]):
        print("Správné písmeno.")
    else:
        print("Špatné písmeno")
else:
    print("Špatná vstupní hodnota")

