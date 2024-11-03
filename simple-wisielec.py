import sys

no_of_tries = 5
word = 'karolina'
used_letters = []

user_word = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)


    return indexes


def show_state_of_game():
    print()
    print(user_word)
    print('Pozostało prób:', no_of_tries)
    print('Użyte litery: ', used_letters)
    print()

###


#gdy nie uzywamy danej zmiennej nie wykorzystujemy w petli to dajemy _, zeby przejsc przez cale slowo
for _ in word:
    user_word.append('_')

while True:
    letter = input('Podaj literę: ')
    used_letters.append(letter)

    found_indexes = find_indexes(word,letter)

    #gdy nie znalazlam zadnego indeksu i usuwam liczbe prob i sprawdzamy czy lisba prob 0 i konczymy gre 
    if len(found_indexes) == 0:
        print('Nie ma takiej litery.')
        no_of_tries -= 1
        # print('Pozostało prób: ', no_of_tries)

        if no_of_tries == 0:
            print('Koniec gry')
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

        # #slowo w postaci listy
        # print(user_word)

        #slowo w postaci stringa
        if "".join(user_word) == word:
            print('Brawo, to jest to słowo!')
            sys.exit(0)

    show_state_of_game()


    # print(f'Użyte litery: {used_letters}')
