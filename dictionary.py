from pprint import pprint

class Node(object):

    # Initializes empty node
    def __init__(self):
        self.end_word = False
        self.words_after = 0
        self.score = 0
        self.children = {chr(letter): None for letter in xrange(ord('a'), ord('z') + 1)}

    def update_word_count(self):
        for letter in xrange(ord('a'), ord('z') +1):
            next_node = self.children[chr(letter)]
            if next_node is not None:
                self.words_after += next_node.update_word_count()
        if self.end_word:
            return 1 + self.words_after
        else:
            return self.words_after

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
        for next_letter in xrange(ord('a'), ord('z') + 1):
            self.dict_to_list_R(dict_list,
                                node.children[chr(next_letter)],
                                word + chr(next_letter))

    def print_dict(self):
        pprint(self.dict_to_list())

    def update_word_count(self):
        self.root.update_word_count()

    def size(self):
        return self.root.words_after
