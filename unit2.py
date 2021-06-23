#problem:The program works as follows:
# you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
# The computer makes guesses, and you give it input - is its guess too high or too low?
# Using bisection search, the computer will guess the user's secret number!
# number=int(input('enter your number between 0 and 100'))
# high=100
# low=0
# while True:
#     ans=(high+low)/2
#     answer=input('Is your secret number '+str(round(ans,0))+'?')
#     if answer=='h':
#         high=ans
#     elif answer=='l':
#         low=ans
#     elif answer=='c':
#         print('Your secret number was: ' + str(int(ans)))
#         break
#     else:
#         print('Sorry, I did not understand your input. Is your secret number '+str(ans)+'?')

# import math
def gcdIter ( a, b ):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    high = max(b,a)
    low = min(b,a)
    residual = high % low
    divisor = int(high / low)
    if residual == 0:
        output = low
    else:
        output = gcdIter(residual, low)
    return output

print(gcdIter(1071,462))

