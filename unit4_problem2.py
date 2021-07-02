def Update_Hand(hand: dict, word: str) -> dict:
    """
    uses up the letters in the given word
    and returns the new hand, without those letters in it
    Args:
        hand:  (string -> int), has all the letters in word. this assumes that however many times a letter appears in 'word',
        'hand' has at least as many of that letter in it.
        word: string

    Returns:
        dictionary without the letters which are in words

    """
    hands = hand.copy()
    for letter in word:
        hands[letter] = hands.get(letter, 0) - 1
    return hands


print(Update_Hand({'d': 1, 'o': 1, 'g': 1}, 'dog'))
