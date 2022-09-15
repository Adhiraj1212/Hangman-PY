import random
import hangman_art  # importing modules
import hangman_words    #importing file with words

print(hangman_art.logo)  # printing variable of module

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
list_chosen_word = list(chosen_word)

# print(f'Pssst, the solution is {chosen_word}.')

display = []
guesses = []

lives = 6

leng = len(chosen_word)
for gues in range(0, leng):
    display.append('_')
print(display)

if lives != 0:
    while lives <= 6 and lives != 0 and '_' in display:
        inp = input("Guess the letter: ")
        guess = inp.lower()

        for ind, letter in enumerate(chosen_word):  # enumerate gives the index value and word value of list

            if letter == guess:
                display[ind] = letter

            else:
                pass

        if guess not in list_chosen_word and guess not in guesses:
            lives -= 1
            print(
                f"Sorry you have guessed the wrong letter. The letter {guess} is not in the word. Now you have {lives} lives remaining")

        if guess in guesses:
            print("You have already guessed the letter")

        guesses.append(guess)

        print(display)
        print(hangman_art.stages[lives])

if lives == 0 and '_' in display:
    print(f"Sorry, You lost. The word was {chosen_word}")
if lives != 0 and '_' not in display:
    print("Congratulations, You have won")
