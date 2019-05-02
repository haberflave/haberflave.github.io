#--------------------WordUP---------------------------
#-----------------------V.1---------------------------
#-----------------------------------------------------
#-----------------------------------------------------
#------------------all rights and credits coming soon-
black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
blue = lambda text: '\033[0;34m' + text + '\033[0m'
magenta = lambda text: '\033[0;35m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
white = lambda text: '\033[0;37m' + text + '\033[0m'

f = open('WordUP/dictionary.txt', 'r+')
dictionary_list = f.read()
f.close()
dictionary = dictionary_list.splitlines()

f = open('WordUP/simple_words.txt', 'r+')
simple_list = f.read()
f.close()
simple_words = simple_list.split(", ")

f = open('WordUP/medium_words.txt', 'r+')
m_words_list = f.read()
f.close()
m_words = m_words_list.splitlines()

f = open('WordUP/hard_words2.txt', 'r+')
hard_words_list = f.read()
f.close()
hard_words = hard_words_list.splitlines()

dic2 = dictionary + simple_words + m_words + hard_words

import time
import random
from datetime import date
today = str(date.today())
import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index + 1
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
from pygame import mixer

sound = 'WordUP/Native.mp3'
mixer.init()
mixer.music.load(sound)
mixer.music.play(-1)

replay = True
print("This is a " + yellow("VOCABULARY") + " game.")
print("Use the " + yellow("ALPHABETICAL") + " hints")
print("to find the " + yellow("SECRET WORD") + ". ")
print("To give up, enter " + red("'I GIVE UP'") + ".")

while replay is True:
    guess = ""
    guess_count = 0
    gave_up = False
    game_play = True
    skill = False
    time_score = ""

    print("To start the game, enter your name: ")
    name = input("")

    while len(name) != 8:
        if len(name) < 8:
            name = name + " "

        else:
            print()
            print()
            print(red("Right now names can not be longer than 8 letters."))
            print()
            print("To start the game, enter a shorter name: ")
            name = input("")

    print("Enter: ")
    print("......1 for " + green("EASY"))
    print("......2 for " + yellow("MEDIUM"))
    print("......3 for " + red("HARD"))

    game_mode = input("")
    start = int(time.time())
    while game_mode != "1" and game_mode != "2" and game_mode != "3":
        print("please enter 1, 2, or 3.")
        game_mode = input("")



    else:
        if int(game_mode) == 1:
            secret_word = random.choice(simple_words)
            while len(secret_word) > 6:
                secret_word = random.choice(simple_words)
            skill = True
            mixer.music.stop()
            sound = 'WordUP/Stars.mp3'
            mixer.init()
            mixer.music.load(sound)
            mixer.music.play(-1)
        elif int(game_mode) == 2:
            secret_word = random.choice(m_words)
            while len(secret_word) < 6 > 9:
                secret_word = random.choice(m_words)
            skill = True
            mixer.music.stop()
            sound = 'WordUP/Resistors.mp3'
            mixer.init()
            mixer.music.load(sound)
            mixer.music.play(-1)
        elif int(game_mode) == 3:
            secret_word = random.choice(hard_words)
            while len(secret_word) < 9:
                secret_word = random.choice(hard_words)
            skill = True
            mixer.music.stop()
            sound = 'WordUP/Ascending.mp3'
            mixer.init()
            mixer.music.load(sound)
            mixer.music.play(-1)



    while game_play is True and guess.lower() != secret_word:
        if guess_count == 0:
            print()
            guess = input("What word am I thinking of?: ")
            guess_count += 1
        else:
            if guess.lower() != str("i give up"):
                if guess.lower() not in dic2:
                    print("That is not a real word: ")
                    guess = input("Guess again: ")
                else:
                    if str(guess)[0:] > str(secret_word[0:]):
                        print("My word comes, " + yellow("before " + guess) + ".")
                        guess = input("Guess again: ")
                        guess_count += 1
                    else:
                        print("My word comes, " + red("after " + guess) + ".")
                        guess = input("Guess again: ")
                        guess_count += 1
            else:
                print()
                game_play = False
                gave_up = True

    else:
        if gave_up is True:
            guess_count = str("FAIL")
            print("You lose! my word was " + red((secret_word.upper())) + ".")
            print("You should work on your vocabulary.")
        else:
            if guess_count == 1:
                print()
                print(red("HOLLY SH*T") + ", How did you get that on your" + red(" very first guess") + "?")
                print("You must be some kind of evil genius.. get out of my head, " + name + ".")
            else:
                if guess_count <= 15:
                    print()
                    print(green("YOU GOT IT!") + " It ony took you " + str(guess_count) + " tries.")
                    print(yellow("That's pretty good there, " + name + "."))
                else:
                    if guess_count >= 16 <= 24:
                        print()
                        print(green("That's it!") + " It took you " + str(guess_count) + " guesses.")
                        print("I bet you can do better next time.")
                    else:
                        if guess_count >= 25:
                            print()
                            print(blue("Way to keep at it, " + name + "...")
                                  + " It took you " + str(guess_count) + " guesses.")
                            print("Ive seen better scores, but hey, at least you didn't give up.")
    score = guess_count
    from operator import itemgetter

    mixer.music.stop()
    sound = 'WordUP/Native.mp3'
    mixer.init()
    mixer.music.load(sound)
    mixer.music.play(-1)

    e = int(time.time() - start)
    time_score = '{:02d}:{:02d}:{:02d}'.format(e // 3600, (e % 3600 // 60), e % 60)
    print()
    print()
    print(green("NAME:.................." + name))
    print(green("SCORE:.................") + "( " + green(str(score)) + " )")
    print(green("TIME:.................." + time_score))
    print(green("PLAYED ON:............." + today))
    print(green("SECRET WORD:...........") + yellow(str(secret_word.upper())))
    print()

    played_on = str(today)

    if int(game_mode) == 1:
        f = open("WordUP/all_easy_scores.txt", 'a+')
        f.write("NAME: " + str(name) + '\n' + str(score) + '\n' +
                "TIME: " + str(time_score) + '\n' +
                "PLAYED ON: " + str(played_on) + '\n' +
                "SECRET WORD: " + str(secret_word) + '\n' + '\n')

        f.close()
    elif int(game_mode )== 2:
        f = open("WordUP/all_medium_scores.txt", 'a+')
        f.write("NAME: " + str(name) + '\n' + str(score) + '\n' +
                "TIME: " + str(time_score) + '\n' +
                "PLAYED ON: " + str(played_on) + '\n' +
                "SECRET WORD: " + str(secret_word) + '\n' + '\n')
        f.close()
    else:
        f = open("WordUP/all_hard_scores.txt", 'a+')
        f.write("NAME: " + str(name) + '\n' + str(score) + '\n' +
                "TIME: " + str(time_score) + '\n' +
                "PLAYED ON: " + str(played_on) + '\n' +
                "SECRET WORD: " + str(secret_word) + '\n' + '\n')
        f.close()
    f.close()
    time.sleep(.3)
    print(yellow("__________________________________________________________"))
    time.sleep(.2)
    print(yellow("__") + blue("H") + yellow("___") + blue("H") + yellow("_") + blue("IIIII") + yellow("___") +
          blue("SSSSS") + yellow("__") + blue("CCCCC") + yellow("__") + blue("OOOOO") + yellow("__") + blue("RRRRR") +
          yellow("__") + blue("EEEEE") + yellow("__") + blue("SSSSS") + yellow("__"))
    time.sleep(.2)
    print(yellow("__") + blue("H") + yellow("___") + blue("H") + yellow("___") + blue("I") + yellow("_____") +
          blue("S") + yellow("______") + blue("C") + yellow("___") + blue("C") + yellow("__") +
          blue("O") + yellow("___") + blue("O") + yellow("__") + blue("R") + yellow("___") + blue("R") +
          yellow("__") + blue("E") + yellow("______") + blue("S") + yellow("______"))
    time.sleep(.2)
    print(yellow("__") + blue("HHHHH") + yellow("___") + blue("I") + yellow("_____") + blue("SSSSS") + yellow("__") +
          blue("C") + yellow("______") + blue("O") + yellow("___") + blue("O") + yellow("__") + blue("RRRR") +
          yellow("___") + blue("EEEEE") + yellow("__") + blue("SSSSS") + yellow("__"))
    time.sleep(.2)
    print(yellow("__") + blue("H") + yellow("___") + blue("H") + yellow("___") + blue("I") + yellow("_________") +
          blue("S") + yellow("__") + blue("C") + yellow("___") + blue("C") + yellow("__") + blue("O") + yellow("___") +
          blue("O") + yellow("__") + blue("R") + yellow("___") + blue("R") + yellow("__") + blue("E") +
          yellow("__________") + blue("S") + yellow("__"))
    time.sleep(.2)
    print(yellow("__") + blue("H") + yellow("___") + blue("H") + yellow
        ("_") + blue("IIIII") + yellow("___") + blue("SSSSS") + yellow("__") + blue("CCCCC") + yellow("__") +
          blue("OOOOO") + yellow("__") + blue("R") + yellow("___") + blue("R") + yellow("__") + blue("EEEEE") +
          yellow("__") + blue("SSSSS") + yellow("__"))
    time.sleep(.2)
    print(yellow("__________________________________________________________"))
    time.sleep(.3)
    print()

    import pickle
    if int(game_mode) == 1:
        pickle_in = open("WordUP/top_easy_scores.pkl", "rb")
        top_easy_scores = pickle.load(pickle_in)
        high_scores = top_easy_scores

        new_high_scores = sorted(high_scores, key=itemgetter(1), )

        if guess_count == "FAIL":
            print(green("Sorry. You don't get a score for giving up. :("))
            print()
            print(yellow("NAME:...SCORE:...TIME:.......DATE:........WORD:"))
            print(blue("-----------------------------------------------"))
            print_high_scores = sorted(high_scores, key=itemgetter(1), )
            for item in print_high_scores[:10]:
                time.sleep(.3)
                print(yellow(str(item)))


        else:

            if int(score) < int((new_high_scores[0][1])):
                print(green("YOU GOT THE NEW HIGH SCORE!"))
                print(green("......GAME MODE: EASY......"))
                print()
                print(yellow("NAME:...SCORE:...TIME:.......DATE:........WORD:"))
                print(blue("-----------------------------------------------"))
            elif int(score) < int((new_high_scores[9][1])):
                print(green("...YOU MADE THE TOP 10!...."))
                print(green("...GAME MODE: EASY........."))
                print()
                print(yellow("NAME:...SCORE:...TIME:.......DATE:........WORD:"))
                print(blue("-----------------------------------------------"))
            high_scores.append([name.upper(), score, time_score, played_on + ": ", secret_word.upper()])
            print_high_scores = sorted(high_scores, key=itemgetter(1), )
            for item in print_high_scores[:10]:
                time.sleep(.3)
                print(yellow(str(item)))

                pickle_out = open("WordUP/top_easy_scores.pkl", "wb")
                pickle.dump(high_scores, pickle_out)
                pickle_out.close()

    elif int(game_mode) == 2:
        pickle_in = open("WordUP/top_medium_scores.pkl", "rb")
        top_medium_scores = pickle.load(pickle_in)
        high_scores = top_medium_scores

        new_high_scores = sorted(high_scores, key=itemgetter(1), )

        if guess_count == "FAIL":
            print(green("Sorry. You don't get a score for giving up. :("))
            print()
            print(yellow("NAME:...SCORE:...TIME:.......DATE:........WORD:"))
            print(blue("-----------------------------------------------"))
            print_high_scores = sorted(high_scores, key=itemgetter(1), )
            for item in print_high_scores[:10]:
                time.sleep(.3)
                print(yellow(str(item)))


        else:

            if int(score) < int((new_high_scores[0][1])):
                print(green("YOU GOT THE NEW HIGH SCORE!"))
                print(yellow(".....GAME MODE: MEDIUM....."))
                print()
                print(yellow("NAME:...SCORE:...TIME:.......DATE:........WORD:"))
                print(blue("-----------------------------------------------"))
            elif int(score) < int((new_high_scores[9][1])):
                print(green("...YOU MADE THE TOP 10!..."))
                print(yellow("...GAME MODE: MEDIUM......"))
                print()
                print(yellow("NAME:...SCORE:...TIME:.......DATE:........WORD:"))
                print(blue("-----------------------------------------------"))
            high_scores.append([name.upper(), score, time_score, played_on + ": ", secret_word.upper()])
            print_high_scores = sorted(high_scores, key=itemgetter(1), )
            for item in print_high_scores[:10]:
                time.sleep(.3)
                print(yellow(str(item)))

                pickle_out = open("WordUP/top_medium_scores.pkl", "wb")
                pickle.dump(high_scores, pickle_out)
                pickle_out.close()

    else:

        pickle_in = open("WordUP/top_hard_scores.pkl", "rb")
        top_hard_scores = pickle.load(pickle_in)
        high_scores = top_hard_scores

        new_high_scores = sorted(high_scores, key=itemgetter(1), )

        if guess_count == "FAIL":
            print(green("Sorry. You don't get a score for giving up. :("))
            print()
            print(yellow("NAME:...SCORE:...TIME:.......DATE:........WORD:"))
            print(blue("-----------------------------------------------"))
            print_high_scores = sorted(high_scores, key=itemgetter(1), )
            for item in print_high_scores[:10]:
                time.sleep(.3)
                print(yellow(str(item)))


        else:

            if int(score) < int((new_high_scores[0][1])):
                print(green("YOU GOT THE NEW HIGH SCORE!"))
                print(red("......GAME MODE: HARD......"))
                print()
                print(yellow("NAME:...SCORE:...TIME:.......DATE:........WORD:"))
                print(blue("-----------------------------------------------"))
            elif int(score) < int((new_high_scores[9][1])):
                print(green("...YOU MADE THE TOP 10!..."))
                print(red("...GAME MODE: HARD........"))
                print()
                print(yellow("NAME:...SCORE:...TIME:.......DATE:........WORD:"))
                print(blue("-----------------------------------------------"))
            high_scores.append([name.upper(), score, time_score, played_on + ": ", secret_word.upper()])
            print_high_scores = sorted(high_scores, key=itemgetter(1), )
            for item in print_high_scores[:10]:
                time.sleep(.3)
                print(yellow(str(item)))

                pickle_out = open("WordUP/top_hard_scores.pkl", "wb")
                pickle.dump(high_scores, pickle_out)
                pickle_out.close()

    print()
    print(green("NAME:.................." + name))
    print(green("SCORE:.................") + "( " + green(str(score)) + " )")
    print(green("TIME:.................." + time_score))
    print(green("PLAYED ON:............." + today))
    print(green("SECRET WORD:...........") + yellow(str(secret_word.upper())))
    print()

    print(green("Play again? "))
    again = input(yellow(": "))
    is_replay = True
    while is_replay is True:
        if again.lower() not in ["y", "yes", "n", "no"]:
            again = input("please enter y/n: ")
        else:
            if again.lower() == "y" or again.lower() == "yes":
                replay = True
                is_replay = False
                score_count = 0
                guess = ""
                break
            if again.lower() == "n" or again.lower() == "no":
                replay = False
                is_replay = False
                break
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()

else:
    print(red("Goodbye!"))
#
# Thanks for
# Playing!!!_________________________________ thehambonehooligan@gmail.com
