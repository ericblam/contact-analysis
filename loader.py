from dictionary import Dictionary
import re

# Loads words in specified file into a dictionary
# Words are only considered characters from a to z, lowercase
def file_to_dict(path):
    word_file = open(path, 'r')
    dictionary = Dictionary()

    for line in word_file:
        if re.match('^[a-z]+$',line) is not None:
            dictionary.add_word(line.strip())

    dictionary.update_word_count()
    word_file.close()
    return dictionary
