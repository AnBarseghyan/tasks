def Play_Game(wordList: list):
    """
    Allow the user to play an arbitrary number of hands.
    Args:
        wordList: all available words

    Returns:
        print the results of the game
    """
    choice = ''
    hand = ''
    while True:
        choice = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if choice == 'n':
            hand = dealHand(HAND_SIZE)
            Play_Hand(hand, wordList, HAND_SIZE)
        elif choice == 'r':
            if hand == '':
                print("You have not played a hand yet. Please play a new hand first!")
                continue
            Play_Hand(hand, wordList, HAND_SIZE)
        elif choice == 'e':
            break
        else:
            print("Invalid command.")
