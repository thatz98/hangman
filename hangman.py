import string
from words import words
from get_word import get_word
from draw_man import draw_man


def hangman():
    word = get_word(words).upper()
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    letter_set = set(word)
    word_letters = {}
    current_letters = list()
    incorrect_count = 0
    for i in range(0, len(word)):
        letter_key = word[i]
        if i not in word_letters:
            word_letters[i] = []
        word_letters[i].append(letter_key)
        current_letters.append("_")

    current_word = ' '.join(current_letters)

    while incorrect_count < 6 or len(letter_set) != 0:
        print(f"\tGuess the word : {current_word}\n")
        input_letter = input('\tGuess a letter : ').upper()
        if input_letter not in alphabet:
            print("\tInvalid input! Enter again.\n")
            continue
        if input_letter in used_letters:
            print('\tAlready guessed that letter! try something else\n')
        elif input_letter in letter_set:
            matching_list = get_keys(word_letters, [input_letter])
            print("\tCorrect! It's there...\n")
            for key in matching_list:
                current_letters[key] = ''.join(word_letters[key])

            current_word = ' '.join(current_letters)
            used_letters.add(input_letter)
            letter_set.remove(input_letter)
            used_str = " , ".join(used_letters)
            print(f"\tUsed letters are: {used_str}\n")

            if len(letter_set) == 0:
                print("""                                                                    

        ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗
        ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║
         ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║
          ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║
           ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║
           ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝

        """)
                print(f"\tThe word is : {current_word}\n")
                return
        else:
            print("\tIncorrect guess! Try again")
            used_letters.add(input_letter)
            incorrect_count += 1
            draw_man(incorrect_count)
            used_str = " , ".join(used_letters)
            print(f"\tUser letters are: {used_str}\n")
            if incorrect_count == 6:
                print("\tSorry, you are dead!!!\n")
                print(f"\tThe word is : {current_word}\n")
                return


# function to return key for any value
def get_keys(word_letters, val):
    keys = set()

    for key, value in word_letters.items():
        if val == value:
            keys.add(key)

    return keys
