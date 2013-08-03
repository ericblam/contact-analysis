from pprint import pprint

letter_list = [chr(l) for l in xrange(ord('a'), ord('z') + 1)]

class Node(object):

    # Initializes empty node
    def __init__(self):
        self.end_word = False
        self.words_after = 0
        self.score = 0
        self.children = {letter: None for letter in letter_list}

    def no_words_after(self):
        for letter in letter_list:
            if self.children[letter] is not None:
                return False
        return True

    def update_word_count(self):
        if self.end_word and self.no_words_after():
            self.words_after = 1
            return 1
        
        n = 0
        for letter in letter_list:
            next_node = self.children[letter]
            if next_node is not None:
                n += next_node.update_word_count()
        if self.end_word:
            self.words_after = n
            return 1 + self.words_after
        else:
            return n

    def update_scores(self, previous_score):
        if self.end_word:
            self.score = previous_score
        for letter in letter_list:
            if self.children[letter] is not None:
                self.children[letter].update_scores(self.words_after + previous_score)
        return

class Dictionary(object):

    # Initializes empty tree
    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        curr = self.root
        for letter in word:
            if curr.children[letter] is None:
                curr.children[letter] = Node()
            curr = curr.children[letter]
        curr.end_word = True

    def dict_to_list(self):
        temp_list = []
        self.dict_to_list_R(temp_list, self.root, '')
        temp_list.sort()
        return temp_list

    def dict_to_list_R(self, dict_list, node, word):
        if node is None:
            return
        if node.end_word:
            dict_list.append(word)
        for next_letter in letter_list:
            self.dict_to_list_R(dict_list,
                                node.children[next_letter],
                                word + next_letter)

    def print_dict(self):
        pprint(self.dict_to_list())

    def update_word_count(self):
        self.root.update_word_count()

    def size(self):
        return self.root.words_after

    def score(self):
        self.update_word_count()
        self.root.update_scores(0)

    # Checks the score of a provided word
    def word_score(self, word):
        curr = self.root
        for letter in word:
            if curr.children[letter] is None:
                print 'Word does not exist'
                return
            else:
                curr = curr.children[letter]
        if curr.end_word:
            return curr.score
        else:
            print "Word does not exist"
