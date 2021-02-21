import random
import pandas as pd
import unicodedata


def hangman():
    csv_collection = 'collection.csv'
    data = pd.read_csv(csv_collection)

    movies = data['TITLE']

    lives = 0
    print('\nWelcome to the hangmans game. At what difficulty do you want to play?\n1) Easy \n2) Medium \n3) Hard')
    print('\nSelect a number')
    difficulty = input()
    if int(difficulty) == 1:
        lives = 10
    elif int(difficulty) == 2:
        lives = 5
    elif int(difficulty) == 3:
        lives = 3

    print('\nLet me think in a movie...\nGot it! \n')
    movie = random.choice(movies).upper()
    movie = unicodedata.normalize("NFKD", movie).encode("ascii", "ignore").decode("ascii")

    letters_movie_initial = []
    for element in movie:
        letters_movie_initial.append(element)

    for element in range(0, len(letters_movie_initial)):
        if letters_movie_initial[element] != ' ' and letters_movie_initial[element] != ':' and \
                letters_movie_initial[element] != '.' and letters_movie_initial[element] != "'" and \
                letters_movie_initial[element] != '(' and letters_movie_initial[element] != ')' and \
                letters_movie_initial[element] != '-':
            letters_movie_initial[element] = '_'

    counter_blank = 0
    for caract in letters_movie_initial:
        if caract == '_':
            counter_blank = counter_blank + 1

    letters_movie_initial1 = ''.join(letters_movie_initial)
    print('This is the movie:\n' + letters_movie_initial1)

    used_letters = []
    game_round = 1
    counter = 0

    while lives > 0 and counter < counter_blank:
        print('\n· ROUND ' + str(game_round))
        print('\tUsed letters: ' + '-'.join(used_letters))
        print('\tLives: ' + str(lives))
        print('\tWrite a letter: ')
        letter = input().upper()

        if letter not in used_letters:
            used_letters.append(letter)
            if letter in movie:
                print('\tCorrect')
                for element in range(0, len(movie)):
                    if movie[element] == letter:
                        letters_movie_initial[element] = letter
                        counter = counter + 1
                letters_movie_initial1 = ''.join(letters_movie_initial)
                print(letters_movie_initial1)
            else:
                print('\tNo, that letter is not in the movie')
                lives = lives - 1
            game_round = game_round + 1
        else:
            print("\tYou've already use that letter")

    if lives == 0:
        print('\nYou died, sorry. The movie was', movie)
    else:
        print('\nYAY! You guessed the movie!')
    print('Do you want to play again? \n1) YES \n2) NO')
    answer = int(input())
    if answer == 1:
        hangman()
    else:
        print('Okey, bye!')
        exit(0)


if __name__ == '__main__':
    hangman()
