import cProfile, pstats, io
# def profile(fnc):
#     def inner(*args, **kwargs):
#
#         pr=cProfile.Profile()
#         pr.enable()
#         retval = fnc(*args, **kwargs)
#         pr.disable()
#         s=io.StringIO()
#         sortby='cumulative'
#         ps=pstats.Stats(pr, stream=s).sort_stats(sortby)
#         ps.print_stats()
#         print(s.getvalue())
#         return retval
#
#

import unit3_problem1
import string


def get_available_letters ( lettersGuessed: list ) -> str:
    '''
    show letters which have no yet been guessed
    lettersGuessed: what letters have been guessed so far
    returns:  letters which have no yet been guessed.
    '''
    all_letters = list(string.ascii_lowercase)
    for x in frozenset(lettersGuessed):
        del (all_letters[all_letters.index(x)])
    return ''.join(all_letters)


print(get_available_letters(['a', 'b', 'e', 'k', 'l']))

