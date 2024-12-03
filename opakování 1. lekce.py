print("Prvních 5 písmen")
print("indexování"[:5])
print("Posledních 5 písmen")
print("indexování"[-5:])
print("Každé 3. písmeno")
print("indexování"[::3])
#převaděč jednotek 
#převodní poměry
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26
#počet jednotek, který má být převeden
kg_pocet= 80
km_pocet = 54
l_pocet = 5
#výpočty
kg_vysledek = (kg_lb * kg_pocet)
km_vysledek = (km_mile * km_pocet)
l_vysledek = (l_gal * l_pocet)
#výsledky
print(kg_pocet, "kg je", kg_vysledek, "lb")
print(km_pocet, "km je", km_vysledek, "mil")
print(l_pocet, "l je", l_vysledek, "gal")
#ceník 
mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000
#sleva
sleva_merc = 5000
# 2x mercedes
cena_2_merc = 2*(mercedes)
#mercedes + rolls
cena_merc_a_rolls = (mercedes + rolls_royce)
#2x rolls plus vybava
cena_2_rolls_s_vybavou = 2*(rolls_royce + vybava)
#mercedes s výbavou 
cena_merc_s_vybavou = (mercedes + vybava)
#mercedes sleva
merc_se_slevou = (mercedes - sleva_merc)
print("Ceník")
print("Sleva na mercedes je", sleva_merc)
print("Cena za dva mercedesy je", cena_2_merc)
print("Cena za Mercedes a Rolls-Royce je", cena_merc_a_rolls)
print("Cena za dva Rolls_Royce s příplatkovou výbavou je", cena_2_rolls_s_vybavou )
print("Cena za mercedes s příplatkovou výbavou je", cena_merc_s_vybavou)
print("Cena za Mercedes po slevě je", merc_se_slevou)
#ulož jméno Lukáš
jmeno = "Lukáš"
prijmeni = "Dvořák"
cele_jmeno = (jmeno + " " + prijmeni)
delka_jmena = len(cele_jmeno)
print("=" * delka_jmena)
print(cele_jmeno)
print("=" * delka_jmena)