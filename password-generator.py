import sys
import random
import string

password = []
characters_left = -1

def update_characters_left(number_of_characters):
    #korzystanie ze zmiennej globalnej
    global characters_left
    if number_of_characters < 0 or number_of_characters > characters_left:
        print('Liczba znaków spoza przedziału 0,', characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print('Pozostało znaków: ', characters_left)

password_length = int(input('Jak długie ma być hasło? '))

if password_length < 5:
  print('Hasło musi mieć min. 5 znaków, spróbuj jeszcze raz.')
  sys.exit(0)
else:
    characters_left = password_length
  
lowercase_letters = int(input('Ile małych liter ma mieć hasło?'))
update_characters_left(lowercase_letters)
#wrzucone do funkcji
# if lowercase_letters < 0 or lowercase_letters > characters_left:
#     print('Liczba znaków spoza przedziału 0,', characters_left)
#     sys.exit(0)
# else:
#     characters_left -= lowercase_letters


uppercase_letters = int(input('Ile dużych liter ma mieć hasło?'))
update_characters_left(uppercase_letters)
#wrzucone do funckji
# if uppercase_letters < 0 or uppercase_letters > characters_left:
#     print('Liczba znaków spoza przedziału 0,', characters_left)
#     sys.exit(0)
    
    
special_characters = int(input('Ile znaków specjalnych ma mieć hasło?'))
update_characters_left(special_characters)
digits = int(input('Ile cyfr ma mieć hasło?'))
update_characters_left(digits)

#sprawdzam ile wolnych miejsc jeszcze zostalo i jesli cos zostaje to dodaje do malych liter
if characters_left > 0:
    print('Nie wszystkie znaki zostały wykorzystane, hasło zostanie uzupełnione małymi literami.')
    lowercase_letters += characters_left
    
print()
print('Długośc hasła: ', password_length)
print('Małe litery: ', lowercase_letters)
print('Duże litery: ', uppercase_letters)
print('Znaki specjalne: ', special_characters)
print('Cyfry: ', digits)

#konwecja pytonowa , ze gdy nie ma zmiennej to uzywamy _
for _ in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1
 
#wymieszanie liter za pmoca biblioteki random shuffle       
random.shuffle(password)
print('Wygenerowane hasło to: ', ''.join(password))


#inny sybszy i prostszy sposob w 1 lini
# import random
# import string

#join sluzy do tego,ze zmienia liste na string
password = ''.join([random.choice(string.ascii_letters + string.punctuation + string.digits) for _ in range(15)])
print(password)
