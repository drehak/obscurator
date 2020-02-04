'''A collection of auxiliary functions that might be useful.'''
from obscurator import Obscurator
from common import Similarity

def showcase(s):
    '''Showcase all tiers of characters on a given sentence.'''
    print(s)
    for tier in Similarity:
        o = Obscurator(similarities=[tier])
        print(o.substitute(s, chance=1))
