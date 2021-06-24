def is_Word_Guessed(secretWord: str, lettersGuessed: list) -> bool:
    """
    check if the word is guessed
    Args:
        secretWord: the word the user is guessing
        lettersGuessed: what letters have been guessed so far

    Returns:
        True if all the letters of secretWord are in lettersGuessed; False otherwise

    """
    guessed_letter_count = sum([1 for i in secretWord if i in lettersGuessed])
    return guessed_letter_count == len(secretWord)


print(is_Word_Guessed('apple', ['a', 'b', 'e', 'p', 'k','l']))
