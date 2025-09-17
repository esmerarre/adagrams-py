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
    letter_frequency_word = {}
    letter_frequency_hand = {}
    
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

    word_uppercase = word.upper()
    point_sum = 0

    #point lists
    one_point_letters = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T" ]
    two_point_letters = ["D", "G"]
    three_point_letters = ["B", "C", "M", "P"]
    four_point_letters = ["F", "H", "V", "W", "Y"]
    five_point_letters = ["K"]
    eight_point_letters = ["J", "X"]
    ten_point_letters = ["Q", "Z"]

    for letter in word_uppercase:
        if letter in one_point_letters:
            point_sum += 1
        elif letter in two_point_letters:
            point_sum += 2
        elif letter in three_point_letters:
            point_sum += 3
        elif letter in four_point_letters:
            point_sum +=4
        elif letter in five_point_letters:
            point_sum += 5
        elif letter in eight_point_letters:
            point_sum += 8
        elif letter in ten_point_letters:
            point_sum += 10

    if len(word_uppercase) >= 7:
        point_sum += 8

    return point_sum
        

def get_highest_word_score(word_list):
    score_dict = {}

    #build dictionary with words as keys and scores as values
    for word in word_list:
        word_score = score_word(word)
        score_dict[word] = word_score
    
    is_first_word = True
    for word in score_dict.keys():
        if is_first_word: #first word in dictionary obtained for subsequent comparison with next words
            higher_score_word = word
            is_first_word = False
            continue
        if score_dict[word] > score_dict[higher_score_word]: 
            higher_score_word = word
        else:
            for word in score_dict.keys(): #this loop compares each word with the last obtained higher_score_word
                if (score_dict[word] == score_dict[higher_score_word] and 
                    len(word) == 10 or len(higher_score_word) == 10):

                    if len(word) == 10:
                        higher_score_word = word
                        return higher_score_word, score_dict[higher_score_word]
                
                elif (score_dict[word] == score_dict[higher_score_word] and 
                    len(word) < len(higher_score_word)):

                    higher_score_word = word
                    return higher_score_word, score_dict[higher_score_word]
                
    return higher_score_word, score_dict[higher_score_word]