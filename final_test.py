import sys

import pytest

import unit3_problem2

#
# @pytest.mark.skipif(sys.version_info > (2, 9), reason = 'do not use')
# def test_is_Word_Guessed():
#     assert unit3_problem2.is_Word_Guessed('apple', ['a', 'c', 'p', 'l', 'e', 'z']) == True
#     assert unit3_problem2.is_Word_Guessed('apple', ['a', 'o', 'l', 'e', 'z']) == False
#     print(unit3_problem2.is_Word_Guessed('apple', ['a', 'o', 'l', 'e', 'z']), '-------------')
#
#
# @pytest.mark.number
# def test_get_Guessed_Word():
#     assert unit3_problem2.get_Guessed_Word('apple', ['a', 'c', 'p', 'y', 'z']) == 'a p p _ _'
#     assert unit3_problem2.get_Guessed_Word('apple', ['l', 'e', 'p', 'y', 'z']) == '_ p p l e'
#
#
# @pytest.mark.string
# def test_get_Guessed_Word_string():
#     result = unit3_problem2.get_Guessed_Word('apple', ['a', 'c', 'p', 'y', 'z'])
#     assert type(result) is str
#     assert unit3_problem2.get_Guessed_Word('apple', ['a', 'c', 'p', 'y', 'z']) == 'a p p _ _'
#     assert unit3_problem2.get_Guessed_Word('apple', ['l', 'e', 'p', 'y', 'z']) == '_ p p l e'
#

# @pytest.mark.parametrize('strings, lists, result',
#                          [('apple', ['a', 'c', 'p', 'y', 'z'], 'a p p _ _'),
#                           ('key', ['k', 'l', 'y'], 'k _ y'),
#                           ('anna', ['a', 'l', 'p', 'n'], 'a n n a')])
# def test_get_Guessed_Word(strings, lists, result):
#     assert unit3_problem2.get_Guessed_Word(strings, lists) == result
