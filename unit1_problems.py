# problem1

from typing import Dict, List, Union
import time


def get_number_of_vowels(text: str) -> int:
    """
    calculate the number of vowels in text
    Args:
        text: the text

    Returns:
       the number of vowels
    """
    vowels = frozenset(['a', 'e', 'i', 'o', 'u'])
    # num = 0
    # for x in text:
    #     if x in vowels:
    #         num += 1
    #
    num = sum(1 for x in text if x in vowels)
    print(f'Number of vowels: {num}')
    return num


start = time.time()
get_number_of_vowels('annabarseghyan'*100)
print(time.time() - start)

#
# # problem2
# def characters_2 ( s ):
#     num = 0
#     for i in range(len(s) - 2):
#         if s[i:(i + 3)] == 'bob':
#             num += 1
#     print('Number of vowels: ' + str(num))
#
#
# characters_2('azcbobobegghaklbob')
#
#
# # problem3
# def longest_substring ( s ):
#     import string
#     alphabet_string = list(string.ascii_lowercase)
#     options = []
#     seq = s[0]
#     for i in range(len(s) - 1):
#         if alphabet_string.index(s[i + 1]) >= alphabet_string.index(s[i]):
#             seq = seq + s[i + 1]
#         else:
#             seq = s[i + 1]
#         options.append(seq)
#     print('Longest substring in alphabetical order is: ' + str(max(options, key=len)))
#
#
# longest_substring('azcbobobegghakl')
# longest_substring('abcbcd')
