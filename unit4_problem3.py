def Is_Valid_Word(word: str, hand: dict, wordList: list) -> bool:
    """
    check if word is in the wordList and is entirely
    composed of letters in the hand.
    Args:
        word: string
        hand: (string -> int), contains all letters which player said
        wordList: all available words

    Returns:
        True if word is in the wordList, otherwise return False
    """
    hand_copy = hand.copy()
    for letter in word:
        if hand_copy.get(letter, 0) <= 0 or letter not in hand_copy.keys():
            return False
            break
        else:
            hand_copy[letter] -= 1
    if word in wordList:
        return True
    else:
        return False


wordList = ['chayote', 'hammer', 'apple']
print(Is_Valid_Word('chayote', {'a': 1, 'c': 2, 'z': 1, 'y': 1, 'h': 1, 'o': 2, 't': 2, 'u': 2}, wordList))
print(Is_Valid_Word('hammer', {'a': 1, 'm': 2, 'e': 1, 'h': 1, 'r': 1}, wordList))
