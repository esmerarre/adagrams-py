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
    # is_letter_in_hand = []
    # for i in word:
    #     if i in letter_bank:
    #         is_letter_in_hand.append(True)
    # if False in is_letter_in_hand:
    #     return False
    # else: 
    #     return True
    pass
    

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass