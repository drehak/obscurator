'''
An obscurator substituting letters in text for visually similar ones.

To perform substitution, an Obscurator object must be created first.
However, this increases performance on concurrent use.
'''
from collections import defaultdict
from random import choice, random

from alphabets import GREEK, CYRILLIC
from common import Similarity


class Obscurator():
    '''
    An obscurator substituting letters in text for visually similar ones.
    :param alphabets: a list of alphabets to be used
    :param similarities: a list of permitted similarities of letters to be used
    '''
    def __init__(self, alphabets=None, similarities=None):
        alphabets = alphabets or [GREEK, CYRILLIC]
        similarities = similarities or [Similarity.HIGH]
        self.simulacra = defaultdict(list)

        for alphabet in alphabets:
            for similarity in alphabet:
                if similarity in similarities:
                    for char in alphabet[similarity]:
                        self.simulacra[char] += alphabet[similarity][char]

    def substitute(self, s, chance=0.5):
        '''
        Substitute letters in a string for visually similar ones.
        :param s: the string to perform substitution on
        :param chance: a chance to substitute each letter, if possible
        :return: a new string with substituted letters
        '''
        for i in range(len(s)):
            if s[i] in self.simulacra and random() < chance:
                s = s[:i] + choice(self.simulacra[s[i]]) + s[i+1:]
        return s
