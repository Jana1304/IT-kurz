"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jana Lásková
email: janalaskova2@seznam.cz
"""
user_name = input("Enter your username: ")
user_password = input("Enter your password: ")
users = {"bob": "123",
         "ann": "pass123",
         "mike": "password123",
         "liz": "pass123"}

if user_name in users and users[user_name] == user_password:
    print("\nHi, welcome to the text analysis section.")
else:
    print("\nI’m sorry, but it seems that you are not registered.")
    exit()
print("\nHere is your texts for analysis:")

text_1 = """\n1. Fossil Butte Overview:
\nSituated about 10 miles west of Kemmerer
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.\n"""

text_2 = """\n2. Union Pacific Railroad History:
\nThe history of the Union Pacific Railroad
in this region is closely tied to the
construction of the transcontinental
railroad in the 19th century. Railroads
helped to shape economic and cultural
landscapes, facilitating trade and
movement across vast distances.\n"""

text_3 = """\n3. Fossil Discovery at Fossil Butte:
\nFossilized remains of ancient plants and animals
have been discovered in Fossil Butte, providing
evidence of prehistoric ecosystems. These fossils
include fish, insects, and reptiles, which are
remarkably well-preserved, offering scientists
valuable insights into Earth's distant past.\n"""

print(text_1 + text_2 + text_3)
print("\nWhich text would you like to analyze?")
print("\n1. Fossil Butte Overview")
print("\n2. Union Pacific Railroad History")
print("\n3. Fossil Discovery at Fossil Butte")

choices = int(input("\nWhich text would you like to analyze? Enter a number btw. 1 and 3 to select: "))
if choices == 1:
   selected_text = text_1
   print("\nYou have selected 1. Fossil Butte Overview.")
elif choices == 2:
    selected_text = text_2
    print("\nYou have selected 2. Union Pacific Railroad History.")
elif choices == 3:
    selected_text = text_3
    print("\nYou have selected 3. Fossil Discovery at Fossil Butte.")
else:
    print("\nInvalid choice. The program will now exit.")
    exit()

text_split = selected_text.split()
capital_letter_words = [word for word in text_split if word.istitle()]
uppercase_word = [words for words in text_split if words.upper()]
lowercase_word = [lwords for lwords in text_split if lwords.islower()]
numbers_as_word = {"one": 1, "two": 2,
                   "three": 3, "four": 4,
                   "five": 5, "six": 6,
                   "seven": 7, "eight": 8,
                   "nine": 9, "ten": 10,
                   "eleven": 11, "twelve": 12,
                   "thirteen": 13, "fourteen": 14, 
                   "fifteen": 15, "sixteen": 16,
                   "seventeen": 17, "eighteen": 18,
                   "nineteen": 19, "twenty": 20}
count_numbers_as_words = 0
sum_numbers_as_words = 0
for word in text_split:
    word_lower = word.lower()
    if word_lower in numbers_as_word:
        count_numbers_as_words += 1
        sum_numbers_as_words += numbers_as_word[word_lower]

print("The total number of words in the text is: ", len(text_split))
print("The number of words starting with a capital letter is: ", len(capital_letter_words))
print("The number of words written in uppercase is: ", len(uppercase_word))
print("The number of words written in lowercase is: ", len(lowercase_word))
print("The number of numbers written as words is: " , count_numbers_as_words)
print("The sum of all numbers written as words is: ", sum_numbers_as_words)