# pro každý email v listu emailu
# .. vyber email,
# .. označ pouze doménu,
# .. ulož ji do setu.
emailu = ["m.vybiralova@firma.cz", "m.vybiralova@firma2.cz", "m.vybiralova@firma3.cz"]
set_domen = set()
for email in emailu:
    domena = email.split("@")[1].split(".")[0]
    set_domen.add(domena)
    print(set_domen)

spain = {"rozloha": 20_000, "měna": "euro"}
for k, v in spain.items():
    print(k, v)

emails = [
    "m.vybiralova@firma.cz",
    "m.vybiralova@email.cz",
    "m.vybiralova@dobradomena.cz",
    "marie@vybiralova.cz",
    "marie.vybiralova@gmail.com",
]
domeny = list()
for email in emails:
    domeny.append(email.split("@")[1].split(".")[0])
domeny_1 = sorted(list(set(domeny)))
print(domeny_1)

