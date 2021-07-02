SCRABBLE_LETTER_VALUES = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5,
                          'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4,
                          'w': 4, 'x': 8, 'y': 4, 'z': 10}


def get_Word_Score(word: str, n: int) -> int:
    """
    calculate the score for a words, which is the sum of the points
    for letters in the word, multiplied by the length of the word,
    plus 50 points if all n letters are used on the first turn.
    Args:
        word: word of lowercase letters, it will be valid word
        n: hand size required for additional points

    Returns:
        score which is >= 0
    """
    score = sum(SCRABBLE_LETTER_VALUES[text] for text in word) * len(word)
    if len(word) == n:
        return score + 50
    else:
        return score


print(get_Word_Score('triplet', 7))
