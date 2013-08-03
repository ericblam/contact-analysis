from dictionary import Dictionary
import re

# Loads words in specified file into a dictionary
# Words are only considered characters from a to z, lowercase
def file_to_dict(path):
    word_file = open(path, 'r')
    dictionary = Dictionary()

    counter = 0
    for line in word_file:
        if re.match('^[a-z]+$',line) is not None:
            dictionary.add_word(line.strip())
        if counter % 25000 == 0:
            print "Loading Dictionary..."
        counter += 1
    dictionary.update_word_count()
    word_file.close()
    return dictionary
