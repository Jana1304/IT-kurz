user_1 = {}
user_email = {"email": "marek.parek@gmail.com"}
user_1["name"] = "Marek"
user_1["surname"] = "Parek"
user_1.update(user_email)
print("User #01: ", user_1)

#ověření hesla
jmeno = "Marek"
heslo = "1234"
uzivatel = {"Marek": "1234"}
if uzivatel.get(jmeno) == heslo:
    print("Ahoj Marku vítej v aplikaci! Pokračuj...")
else:
    print("Uživatelské jméno nebo heslo nejsou v pořádku!")
#vytvoření setů
cisla_1 = (1, 1, 2, 3, 4)
cisla_2 = (5, 6, 7, 7, 8)
sjednocené_hodnoty = set(cisla_1).union(set(cisla_2))
print("Sjednocené hodnoty ze zadání: ", sjednocené_hodnoty)

cisla_3 = {1, 2, 3, 4}
cisla_4 = {3, 4, 5, 6}
rozdil_cisel = set(cisla_3).difference(set(cisla_4))
print("Rozdílné hodnoty prvního setu oproti druhému: ", rozdil_cisel)
      

