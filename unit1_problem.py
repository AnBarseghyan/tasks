number=int(input('enter your number between 0 and 100'))
high=100
low=0
while True:
    ans=(high+low)/2
    answer=input('Is your secret number '+str(ans)+'?')
    if answer=='h':
        high=ans
    elif answer=='l':
        low=50
    elif answer=='c':
        print('Your secret number was: ' + str(ans))
        break
    else:
        print('Sorry, I did not understand your input. Is your secret number '+str(ans)+'?')

