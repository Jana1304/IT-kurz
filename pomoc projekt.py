TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#omezení hesla?
vstup = None
for _ in range(3):
    vstup = input("Zadej číslo: ")
    if vstup.isdigit():
        break
else:
    exit()
print("Zadal jsi XY")
#nápověda projekt a také někde použití funkce get
#Pokud potřebujete analyzovat jednotlivá slova v textu (například zjistit počet slov psaných velkými písmeny nebo malými písmeny), cyklus for je velmi praktický:

words = text.split()
uppercase_count = 0

for word in words:
    if word.isupper():
        uppercase_count += 1
print("Počet slov psaných velkými písmeny:", uppercase_count)
#Program analyzuje vybraný text a poskytne následující statistiky:
#Počet slov: Celkový počet slov v textu.
#Slova začínající velkým písmenem: Počet slov, která začínají velkým písmenem.
#Slova psaná velkými písmeny: Počet slov psaných kompletně velkými písmeny.
#Slova psaná malými písmeny: Počet slov psaných kompletně malými písmeny.
#Čísla (ne cifry): Počet celých čísel (slov, která jsou čísly).
#Součet všech čísel: Součet všech celých čísel v textu.
choices = int(input("\nWhich text would you like to analyze? "))
text_1_split = text_1.split()
text_1_lower = text_1.lower().split()
capital_letter_words = [word for word in text_1_split if word.istitle()]
uppercase_word = [words for words in text_1_split if words.upper()]
lowercase_word = [lwords for lwords in text_1_split if lwords.islower()]
numbers_as_word = 
print("The total number of words in the text is: ", len(text_1_split))
    print("The number of words starting with a capital letter is: ", len(capital_letter_words))
    print("The number of words written in uppercase is: ", len(uppercase_word))
    print("The number of words written in lowercase is: ", len(lowercase_word))
    print("The number as words is: ", len(numbers_as_words_1))
    print("The sum of all numbers written as words is: 0")")