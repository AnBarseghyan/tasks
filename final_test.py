import pytest
import for_testing
import sys

@pytest.mark.skipif(sys.version_info < (2, 9), reason = 'do not use')
def test_is_Word_Guessed():
    assert for_testing.is_Word_Guessed('apple', ['a', 'c', 'p', 'l', 'e', 'z']) == True
    assert for_testing.is_Word_Guessed('apple', ['a', 'o', 'l', 'e', 'z']) == False
    assert for_testing.get_Guessed_Word('apple', ['l', 'e', 'p', 'y', 'z']) == '_ p p l e'
    print(for_testing.is_Word_Guessed('apple', ['a', 'o', 'l', 'e', 'z']), '-------------')

#
# @pytest.mark.number
# def test_get_Guessed_Word():
#     assert for_testing.get_Guessed_Word('apple', ['a', 'c', 'p', 'y', 'z']) == 'a p p _ _'
#     assert for_testing.get_Guessed_Word('apple', ['l', 'e', 'p', 'y', 'z']) == '_ p p l e'
#
#
# @pytest.mark.string
# def test_get_Guessed_Word_string():
#     result = for_testing.get_Guessed_Word('apple', ['a', 'c', 'p', 'y', 'z'])
#     assert type(result) is str
#     assert for_testing.get_Guessed_Word('apple', ['a', 'c', 'p', 'y', 'z']) == 'a p p _ _'
#     assert for_testing.get_Guessed_Word('apple', ['l', 'e', 'p', 'y', 'z']) == '_ p p l e'
#

# @pytest.mark.parametrize('strings, lists, result',
#                          [('apple', ['a', 'c', 'p', 'y', 'z'], 'a p p _ _'),
#                           ('key', ['k', 'l', 'y'], 'k _ y'),
#                           ('anna', ['a', 'l', 'p', 'n'], 'a n n a')])
# def test_get_Guessed_Word(strings, lists, result):
#     assert for_testing.get_Guessed_Word(strings, lists) == result


from for_testing import students_info
StdInfo = None

def setup_module(module):
    print("-----------setup-----------")
    global StdInfo
    StdInfo = students_info({'Anna': 1, "Liza": 4, "Ara": 3})


def test_get_data():
    assert StdInfo.get_grade('Ara') == 3

def test_best():
    assert StdInfo.best() == "Liza"
