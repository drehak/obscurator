'''A collection of auxiliary functions that might be useful.'''
from obscurator import Obscurator
from common import Similarity

def showcase(s):
    '''Showcase all tiers of characters on a given sentence.'''
    print(s)
    for tiers in [
        [Similarity.HIGH],
        [Similarity.MEDIUM],
        [Similarity.LOW],
        [Similarity.MEDIUM, Similarity.LOW]
    ]:
        o = Obscurator(similarities=tiers)
        print(o.substitute(s, chance=1))
