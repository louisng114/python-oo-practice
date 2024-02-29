"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    """Read words from txt document"""
    def __init__(self, path):
        self.path = path
        self.word_list = self.split_line()

    def __len__(self):
        return len(self.word_list)

    def __repr__(self):
        return f"WordFinder({self.path})"

    def __str__(self):
        return f"{len(self)} words read"

    def random(self):
        return choice(self.word_list)

    def split_line(self):
        f = open(self.path, "r")
        lst = f.read().split("\n")
        f.close()
        return lst

class SpecialWordFinder(WordFinder):
    """Subclass of WordFinder. Ignores empty and comment lines."""
    def __init__(self, path):
        super().__init__(path)
    
    def split_line(self):
        lst = [word for word in super().split_line() if ((word.strip() != "") and (word.startswith("#")))]
        return lst