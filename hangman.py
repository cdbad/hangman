from random import choice

guessed_letters = set()
end = False
wrongs = 0
guessed_word = list()

def hanged():
    '''
     ------\n
     |    |\n
     O    |\n
    /|\   |\n
    / \   |\n
    -------
    '''

    global wrongs, end

    if wrongs == 0:
        return ' ------\n       |\n       |\n       |\n       |\n-------'
    elif wrongs == 1:
        return ' ------\n |     |\n       |\n       |\n       |\n-------'
    elif wrongs == 2:
        return ' ------\n |     |\n O     |\n       |\n       |\n-------'
    elif wrongs == 3:
        return ' ------\n |     |\n O     |\n |     |\n       |\n-------'
    elif wrongs == 4:
        return ' ------\n |     |\n O     |\n/|     |\n       |\n-------'
    elif wrongs == 5:
        return ' ------\n |     |\n O     |\n/|\    |\n       |\n-------'
    elif wrongs == 6:
        return ' ------\n |     |\n O     |\n/|\    |\n/      |\n-------'
    elif wrongs >= 7:
        end = True
        return ' ------\n |     |\n O     |\n/|\    |\n/ \    |\n-------'

def select_word():
    '''chooses a word randomly'''
    global guessed_word
    with open('words.txt', 'r') as reader:
        words = reader.readlines()
    chosen = choice(words).strip().lower()
    guessed_word = ['_' for l in chosen]
    return chosen

def validate_input(letter):
    '''checks that the inputted letter is valid and not already guessed'''
    
    global guessed_letters
    
    if len(letter) != 1:
        return False, '1'
    elif letter in guessed_letters:
        return False, 'guessed'
    
    guessed_letters.add(letter)
    return True

def get_letter(word, letter):
    '''gets the locations of the current guessed letter in the word'''
    global end
    while end == False:
        indexes = [i for i, l in enumerate(word) if l == letter]
        return indexes
    
def guessed(**args):
    '''returns the letters that were already guessed'''
    
    word = args['word']
    global guessed_word, wrongs

    if 'found' in args.keys():
        for i in args['found']:
            guessed_word[i] = word[i]
        if len(args['found']) == 0:
            wrongs += 1
            print(hanged())

def get_player_input(word):
    '''manages player's input'''
    letter = input('Guess a letter: ').lower()
    validation = validate_input(letter)
    global guessed_word, end, wrongs

    if validation == True:
        found_letters = get_letter(word, letter) # list
        
        print(hanged())
        guessed(word=word, found=found_letters)
        print(" ".join(guessed_letters))
    else:
        if validation[1] == '1':
            print("That's not a single letter.")
        else:
            print("You already guessed this letter.")
    
    if not '_' in guessed_word:
        end = True
        print(f'\n{" ".join(guessed_word)}')
    else:
        print(f'\n{" ".join(guessed_word)}')

def main ():
    global guessed_word, end
    selected_word = select_word()
    
    # print(selected_word)
    print(hanged())
    print(" ".join(guessed_word))
    while end == False:
        get_player_input(selected_word)
    if end == True and not "_" in " ".join(guessed_word):
        print('\nYou win!!')
    else:
        print("\nYou lose :(")

main()