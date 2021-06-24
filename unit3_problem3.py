import string
import time
def get_available_letters(lettersGuessed: list) -> str:
    '''
    show letters which have no yet been guessed
    lettersGuessed: what letters have been guessed so far
    returns:  letters which have no yet been guessed.
    '''
    all_letters = list(string.ascii_lowercase)
    for x in frozenset(lettersGuessed):
        del(all_letters[all_letters.index(x)])
    return ''.join(all_letters)


start = time.time()
print(get_available_letters(['a', 'b', 'e',  'k','l']))
print(time.time() - start)
