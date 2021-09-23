import os


def main():
    print_title()
    file_path = input("Please enter the file path you'd like to use: ")
    while not os.path.isfile(file_path):
        file_path = input("Whoops! No such file! Please enter the name of the file you'd like to use: ")
    another_round = 1
    while another_round == 1:
        index = input("choose a random number for your random secret word: ")
        while index.isnumeric() == False:
            index = input("choose a random NUMBER!! NUMBER for your random secret word. type again: ")
        secret_word = choose_word(file_path, index)
        old_letters_guessed = []
        print("lets start!")
        hidden_word = show_hidden_word(secret_word, old_letters_guessed)
        num_of_tries = get_num_of_tries(hidden_word, old_letters_guessed)
        print_hangman(num_of_tries)
        print(hidden_word)

        game_result = check_win(secret_word, old_letters_guessed)
        failed_tries = get_num_of_tries(hidden_word, old_letters_guessed)
        MAX_TRIES = 6

        while game_result == False and failed_tries != MAX_TRIES:
            letter_guessed = input("guess a letter: ")

            while try_update_letter_guessed(letter_guessed, old_letters_guessed) == False:
                letter_guessed = input("invalid letter, please type again: ")

            word_round_1 = show_hidden_word(secret_word, old_letters_guessed)
            if word_round_1 == hidden_word:
                print(":(")
                lenOfMistakes = get_num_of_tries(hidden_word, old_letters_guessed)
                print_hangman(lenOfMistakes)

            hidden_word = word_round_1
            print(hidden_word)

            failed_tries = get_num_of_tries(hidden_word, old_letters_guessed)
            game_result = check_win(secret_word, old_letters_guessed)

        if game_result == True:
            print("\nWIN\n") 
        elif failed_tries == MAX_TRIES:
            print("\nLOSE\n")

        #when game ends- option to play another round\end game.
        another_round = input("do you want to play again ?\n1 = yes\n2 = no\n")
        if another_round.isnumeric() == True:
            another_round = int(another_round)

        if another_round == 2:
            print("thank you for playing!")
            break

        while another_round != 1 and another_round != 2:
            another_round = input("you have only 2 options, 1 or 2. go ahead: \n")
            if another_round.isnumeric() == True:
                another_round = int(another_round)

        if another_round == 2:
            print("thank you for playing!")
            break

        #clears screen for new game
        os.system('clear')
        print_title()


def print_title():
    """printing the title of the game
    return:none"""
    HANGMAN_ASCII_ART = """welcome to the game hangman
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
"""
    print(HANGMAN_ASCII_ART)


def choose_word(file_path, index):
    """the function choosing a word according to the index number from user.
    :param file_path: path to file that contains words divided by " ".
    :type file_Path: string
    :param index: a number choosed by the user.
    :type index: int
    :return: word from file_path
    :rtype: str."""

    opened_file = open(file_path, "r")
    readed_file = opened_file.read()
    opened_file.close()
    readed_file = readed_file.replace("\n", "")
    random_words = readed_file.split(" ")

    random_words_no_duplications = []
    for item in random_words:
        if item not in random_words_no_duplications:
            random_words_no_duplications.append(item)
        else:
            continue

    number_of_words_from_original = int(len(random_words))
    index = int(index) - 1

    new_index = index % number_of_words_from_original

    secret_word = random_words[new_index]

    return secret_word


def show_hidden_word(secret_word, old_letters_guessed):
    """replace letter with "_" if its not in old_letter_guessed.
    :param secret_word: word choosed from file_path.
    :type secret_word: str.
    :param old_letters_guessed: list of valid guessed letters.
    :type old_letters_guessed: list.
    :return: string of secret word with '_' where letter not guessed.
    :rtype: str."""
    copy_secret_word = secret_word
    for letter in secret_word:
        if letter not in old_letters_guessed:
            copy_secret_word = copy_secret_word.replace(letter, " _ ")
    return copy_secret_word


def get_num_of_tries(return_show_hidden_word, old_letters_guessed):
    """the function get the number of wrong tries.
    :param return_show_hidden_word: the correct letters guessed from secret word.
    :type return_show_hidden_word: str.
    :param old_letters_guessed: all the guessed letters included the correct letters.
    :type old_letters_guessed: list.
    :return: the number of wrong tries from the list of old_letters_guessed.
    :rtype: int"""
    wrong_tries = []
    for letter in old_letters_guessed:
        if letter not in return_show_hidden_word:
            wrong_tries.append(letter)
    num_of_tries = len(wrong_tries)
    return num_of_tries


def print_hangman(num_of_tries):
    """the funtion return the picture of hangman according to number of tries.
    :param num_of_tries: the number of wrong tries.
    :type num_of_tries: int.
    :return: the picture of hangman according to the num_of_tries from dict.
    :rtype: str."""

    picture_1 = """x-------x"""

    picture_2 = """
    x-------x
    |
    |
    |
    |
    |"""

    picture_3 = """
    x-------x
    |       |
    |       0
    |
    |
    |"""

    picture_4 = """
    x-------x
    |       |
    |       0
    |       |
    |
    |"""

    picture_5 = """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |"""

    picture_6 = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |"""

    picture_7 = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""
    HANGMAN_PHOTOS = {0: picture_1, 1: picture_2, 2: picture_3, 3: picture_4, 4: picture_5, 5: picture_6, 6: picture_7}
    print(HANGMAN_PHOTOS[num_of_tries])


def is_valid_input(guess_letter):
    """the function returns false if the letter is invalid
    or true if its valid(only 1 letter).
    :param guess_letter: the input of guessed letter.
    :type guess_letter: str.
    :return: true if its valid, fales if its invalid.
    :rtype: boolean."""
    length = len(guess_letter)

    if length > 1 and not guess_letter.isalpha():
        return False
    elif not guess_letter.isalpha():
        return False
    elif length > 1:
        return False
    else:
        return True


def check_valid_input(letter_guessed, old_letters_guessed):
    """the function returns true if the letter typed is valid
    and not typed before.
    :param letter_guessed: the input of letter_guessed from user.
    :type letter_guessed: str.
    :param old_letters_guessed: all the guessed letters included the correct letters.
    :type old_letters_guessed: list.
    :return: true if the letter typed is valid and not typed before\ False.
    :rtype: boolean."""
    if is_valid_input(letter_guessed) == False:
        return False
    elif letter_guessed in old_letters_guessed:
        return False
    elif is_valid_input(letter_guessed) == True and letter_guessed not in old_letters_guessed:
        return True
    else:
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """function adds valid letter to old_letter_gussed list,
    in addition print 'X' and list of sorted old_letters_gussed with -> if not valid
    and returns true if valid or flase if not valid.
    :param letter_guessed: the input of letter_guessed from user.
    :type letter_guessed: str.
    :param old_letters_guessed: all the guessed letters included the correct letters.
    :type old_letters_guessed: list.
    :return:True if check_valid_input true, else false
    :rtype: boolean"""
    letter_guessed = letter_guessed.lower()
    if check_valid_input(letter_guessed, old_letters_guessed) == True:
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        old_letters_guessed.sort()
        print("->".join(old_letters_guessed))
        return False


def check_win(secret_word, old_letters_guessed):
    """the func returns True if the player guessed all the letters in the secret word.
    else, returns False.
    :param secret_word: secret word choosed.
    :type secret_word: str.
    :param old_letters_guessed: list of all guessed letters.
    :type old_letters_guessed: list.
    :return: true if hidden word =  secret_word, false if not.
    :rtype: boolean."""
    if show_hidden_word(secret_word, old_letters_guessed) == secret_word:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
