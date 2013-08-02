import re
from pprint import pprint

class Node(object):

    # Initializes empty node
    def __init__(self):
        self.end_word = False
        self.words_after = 0
        self.score = 0
        self.children = {chr(letter): None for letter in xrange(ord('a'), ord('z') + 1)}

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

    def print_dict(self):
        temp_list = []
        self.R_print_dict(temp_list, self.root, '')
        temp_list.sort()
        pprint(temp_list)

    def R_print_dict(self, dict_list, node, word):
        if node is None:
            return
        if node.end_word:
            dict_list.append(word)
        for next_letter in xrange(ord('a'), ord('z') + 1):
            self.R_print_dict(dict_list,
                              node.children[chr(next_letter)],
                              word + chr(next_letter))

dic = Dictionary()
dic.add_word('word')
dic.add_word('world')
dic.add_word('hello')
dic.add_word('ant')
dic.add_word('antelope')
#pprint(dic.root.children)
dic.print_dict()
