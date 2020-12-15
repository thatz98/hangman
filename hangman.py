import random
import string

from words import words


def get_word(word_list):
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)

    return word


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
    print(f"Guess the word : {current_word}")

    input_letter = input('Guess a letter : ').upper()
    if input_letter in used_letters:
        print('Already guesses that letter! try something else')
    elif input_letter in letter_set:
        matching_list = get_keys(word_letters, [input_letter])
        print("Correct! It's there...")
        for key in matching_list:
            current_letters[key] = ''.join(word_letters[key])

        current_word = ' '.join(current_letters)
        print(f"Current word is : {current_word}")
        used_letters.add(input_letter)
    else:
        print("Incorrect guess! Try again")
        used_letters.add(input_letter)


# function to return key for any value
def get_keys(word_letters, val):
    keys = set()

    for key, value in word_letters.items():
        if val == value:
            keys.add(key)

    return keys


def draw_man(incorrect_count):
    if incorrect_count == 1:
        print()

hangman()