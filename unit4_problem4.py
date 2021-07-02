def calculate_Hand_len(hand: dict) -> int:
    """
    calculate the length (number of letters) in the current hand
    Args:
        hand: dictionary which contains all letter

    Returns: number of letters
    """
    return sum(hand.values())


print(calculate_Hand_len({'x': 1, 'd': 1, 'f': 1, 'r': 2, 'q': 1, 'j': 1, 'g': 1, 'b': 1, 'e': 2, 'c': 1, 'h': 2}))
