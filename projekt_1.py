"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Prchal
email: prchalmartin2@gmail.com
"""
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

# Vyžádá si od uživatele přihlašovací jméno a heslo,zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů, 
user = input("username:")
password = input("password:")
print("----------------------------------------")
# zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů, pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,
registred_users = {
    "bob":123,
    "ann":"pass123",
    "mike":"password123",
    "liz":"pass123"
}
if user in registred_users:
    print("Welcome to the app,", user)
else:
     exit()

# Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS
print("We have 3 texts to be analyzed.")
print("----------------------------------------")
num_text = input("Enter a number btw. 1 and 3 to select: ")
if not (num_text.isdigit() and 1 <= int(num_text) <= 3):
    print("Invalid input. Please enter a number between 1 and 3.")
else:
    num_text = int(num_text)-1
    
selected_text = TEXTS[num_text]
selected_text = selected_text.split(" ")
print("----------------------------------------")
# počet slov
count_words = len(selected_text)

# počet slov psaných velkými písmeny,
uppercase_word = 0
for word in selected_text:
    if word.isupper():
        uppercase_word += 1
print(f"There are  {uppercase_word} uppercase words.")

# počet slov psaných malými písmeny,počet čísel (ne cifer),
lowercase_word = 0
for word in selected_text:
    if word.islower():
        lowercase_word += 1
print(f"There are  {lowercase_word} lowercase words.")

# počet čísel (ne cifer),sumu všech čísel (ne cifer) v textu.
digit_words = 0
for word in selected_text:
    if word.isdigit():
        digit_words += 1
print(f"There are  {digit_words} numeric strings.")

# sumu všech čísel (ne cifer) v textu
sum_of_numbers = 0
current_number = ""

for char in selected_text:
    if char.isdigit():  # Kontrola, zda je znak číslice
        current_number += char  # Přidáme číslici k aktuálnímu číslu
    else:
        if current_number:  # Pokud jsme našli celé číslo (skončila jeho sekvence)
            sum_of_numbers += int(current_number)  # Převedeme na číslo a přičteme
            current_number = ""  # Resetujeme proměnnou pro další číslo

    # Ošetření posledního čísla (pokud text končí číslem)
    if current_number:
        sum_of_numbers += int(current_number)
print("The sum of all the numbers ", sum_of_numbers)

print("""
----------------------------------------
LEN|  OCCURENCES  |NR.
----------------------------------------
""")