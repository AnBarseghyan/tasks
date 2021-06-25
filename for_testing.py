def get_Guessed_Word(secretWord, lettersGuessed):
    """
    show which letters are guessed, which not
    Args:
        secretWord: the word the user is guessing
        lettersGuessed: what letters have been guessed so far

    Returns:
        comprised of letters and underscores that represents what letters in secretWord have been guessed so far

    """
    guess_letters = " ".join([x if x in lettersGuessed else "_" for x in secretWord])
    return guess_letters


print(get_Guessed_Word('apple', ['a', 'c', 'p', 'y', 'z']))


def is_Word_Guessed(secretWord, lettersGuessed):
    """
    check if the word is guessed
    Args:
        secretWord: the word the user is guessing
        lettersGuessed: what letters have been guessed so far

    Returns:
        True if all the letters of secretWord are in lettersGuessed; False otherwise

    """

    return set(secretWord) - set(lettersGuessed) == set()


class students_info:
    def __init__(self, data):
        self.data = data

    def get_grade(self, name):
        for i in self.data.keys():
            if i == name:
                return self.data[i]

    def best(self):
        best = 0
        for i in self.data.keys():
            if self.data[i] > best:
                best = self.data[i]
                name = i
        return name

