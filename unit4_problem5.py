def Play_Hand(hand: dict, wordList: list, n: int):
    """
    Allows the user to play the given hand
    Args:
        hand: letter which player said
        wordList: list of available words
        n:  hand size required for additional points

    Returns:
    """
    point = 0
    word = ''
    while True:
        print('Current Hand: ')
        displayHand(hand)
        word = input('Enter word, or a "." to indicate that you are finished:')
        if word == '.':
            print(f'Goodbye! Total score: {point} points.')
            break
        elif Is_Valid_Word(word, hand, wordList) == False:
            print('Invalid word, please try again.')
        else:
            points += get_Word_Score(word, n)
            print(f'{word} earned {get_Word_Score(word, n)} points. Total: {point} points')
            if len(word) == calculate_Hand_len(hand):
                print(f'Run out of letters. Total score: {point} points.')
                break
            hand = Update_Hand(hand, word)
