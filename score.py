from dictionary import Dictionary

def score(dictionary):
    dictionary.score()

    dict_list = dictionary.dict_to_list()
    score_dict = {}

    for word in dict_list:
        score_dict[word] = dictionary.word_score(word)

    return score_dict

def highest_score(dictionary):
    score_dict = score(dictionary)

    word = ''
    high_score = 0
    for element in score_dict:
        if score_dict[element] > high_score:
            high_score = score_dict[element]
            word = element
    return {'word': word, 'score': high_score}
