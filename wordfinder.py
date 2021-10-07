"""Word Finder: finds random words from a dictionary."""

from random import randint

class WordFinder:
    """Class to return a random word from a list of words

    ---- Example
    Given file test.txt with words:
    porcupine
    owl
    kangaroo
    
    >>> words = WordFinder(filename="test.txt")
    3 words read

    """
    def __init__(self,filename):
        """Initialize list of words from file"""
        self.words = []
        self.populateWordList(filename)
        print(f"{len(self.words)} words read")
    def populateWordList(self,filename):
        """ Helper function to populate word list from file"""
        wordsFile = open(filename, 'r')
        for line in wordsFile:
            self.words.append(line.rstrip())
    def random(self):
        """ Return a random word from the word list
        
        >>> words = WordFinder(filename="test.txt")
        3 words read
        
        >>> words.random() in ['porcupine','owl','kangaroo']
        True
        
        """
        randIndex = randint(0,len(self.words)-1)
        return self.words[randIndex]

class SpecialWordFinder(WordFinder):
    """Initialize special word finder that excludes comments and empty lines
    
    ---- Example
    Given file test2.txt with words:
    porcupine
    #
    owl

    kangaroo
    salmon

    >>> words = SpecialWordFinder(filename="test2.txt")
    4 words read

    """
    def __init__(self,filename):
        """Initialize word list from file"""
        super().__init__(filename)
    def populateWordList(self,filename):
        """ Special helper function to populate word list from file, excluding comments and empty lines"""
        wordsFile = open(filename, 'r')
        for line in wordsFile:
            if line != "\n" and line[0] != "#":
                    self.words.append(line.rstrip())
    



