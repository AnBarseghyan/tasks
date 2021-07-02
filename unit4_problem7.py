def Play_Game(wordList: list):
    """
    play word game with computer or yourself
    Args:
        wordList: all available words

    Returns:
    results of the game
    """
    while True:
        choice_1 = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if choice_1 == 'e':
            break
        elif choice_1 == 'n':
            while True:
                choice_2 = str(input('Enter u to have yourself play, c to have the computer play: '))
                if choice_2 == 'u':
                    hand = dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                    break
                elif choice_2 == 'c':
                    hand = dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print('Invalid command.')
        elif choice_1 == 'r':
            try:
                hand
                choice_2 = str(input('Enter u to have yourself play, c to have the computer play: '))
                if choice_2 == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                elif choice_2 == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)

            except:
                print('You have not played a hand yet. Please play a new hand first!')
        else:
            print('Invalid command.')
