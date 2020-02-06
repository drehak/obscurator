'''Common functionality for multiple modules.'''
from enum import Enum


class Similarity(Enum):
    '''Describes a degree of similarity between a letter and its imitation.'''
    HIGH = 0    # pretty much indistinguishable
    MEDIUM = 1  # lightly bent or altered
    LOW = 2     # severely deformed but still similar
