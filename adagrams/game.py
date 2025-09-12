from random import randint

def draw_letters():
    tiles = [
    'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
    'B', 'B',
    'C', 'C',
    'D', 'D', 'D', 'D', 
    'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 
    'F', 'F', 
    'G', 'G', 'G', 
    'H', 'H',  
    'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 
    'J',  
    'K', 
    'L', 'L', 'L', 'L', 
    'M', 'M', 
    'N', 'N', 'N', 'N', 'N', 'N', 
    'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 
    'P', 'P', 
    'Q', 
    'R', 'R', 'R', 'R', 'R', 'R', 
    'S', 'S', 'S', 'S', 
    'T', 'T', 'T', 'T', 'T', 'T',
    'U', 'U', 'U', 'U', 
    'V', 'V', 
    'W', 'W', 
    'X', 
    'Y', 'Y', 
    'Z'
    ]
    selected_index = []
    picked_letters = []
    for i in range(0, 10):
        rand_selection = randint(0, len(tiles)-1)
        while rand_selection in selected_index:
            rand_selection = randint(0, len(tiles)-1)
        selected_index.append(rand_selection)
        random_letter = tiles[rand_selection]
        picked_letters.append(random_letter)
    return picked_letters


def uses_available_letters(word, letter_bank):
    word_uppercase = word.upper()
    is_letter_in_hand = []
    
    letter_frequency_word = {}
    letter_frequency_hand = {}
    counter = 0
    for i in word_uppercase:
        if i not in letter_bank:
            return False
        else:
            letter_frequency_word[i] = letter_frequency_word.get(i, 0) + 1

    for i in letter_bank:
        letter_frequency_hand[i] = letter_frequency_hand.get(i, 0) + 1
        
    for letter in word_uppercase:
        if letter_frequency_word[letter] > letter_frequency_hand[letter]:
            return False

    return True
        
    
    

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass