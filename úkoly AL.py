username = input("Enter your username: ")
password = input("Enter your password: ")
users = {
     "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
text_1 = """\n1. Fossil Butte Overview:
\nSituated about 10 miles west of Kemmerer
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley."""

text_2 = """\n2. Union Pacific Railroad History:
\nThe history of the Union Pacific Railroad
in this region is closely tied to the
construction of the transcontinental
railroad in the 19th century. Railroads
helped to shape economic and cultural
landscapes, facilitating trade and
movement across vast distances."""

text_3 = """\n3. Fossil Discovery at Fossil Butte:
\nFossilized remains of ancient plants and animals
have been discovered in Fossil Butte, providing
evidence of prehistoric ecosystems. These fossils
include fish, insects, and reptiles, which are
remarkably well-preserved, offering scientists
valuable insights into Earth's distant past."""

if username in users and users[username] == password:
    print("Hi, welcome to the text analysis section.")
elif username in users and users[username] != password:
    print("The password is incorrect.")
    exit()
else:
    print("I’m sorry, but it seems that you are not registered.")
    exit()

print(text_1 + "\n" + text_2 + "\n" + text_3)
print("\nWhich text would you like to analyze?")
print("1. Fossil Butte Overview")
print("2. Union Pacific Railroad History")
print("3. Fossil Discovery at Fossil Butte")

words = text_1.split()
uppercase_words = [word for word in words if word.isupper()]
capital_letter = [word for word in words if word.istitle()]
lowercase_word = [word for word in words if word.islower()]
count_numbers = 0

choices = int(input("Which text would you like to analyze? (1, 2, 3): "))
if choices == 1:
    print("You have selected 1. Fossil Butte Overview.")
    print("The total number of words in the text is: ", len(text_1))
    print("The number of words starting with a capital letter is: ", len(capital_letter))
    print("The number of words written in uppercase is: ", len(uppercase_words))
    print("The number of words written in lowercase is: ", len(lowercase_word))
    for word in words:
        if word.isdigit():
            count_numbers += 1
            print("The number of numbers is :", count_numbers)

