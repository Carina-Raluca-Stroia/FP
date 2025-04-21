# 10. The palindrome of a number is the number obtained by reversing the order of its digits (e.g. the palindrome of 237 is 732).
# For a given natural number n, determine its palindrome.

# function that checks if a nr is a palindrome or not
def palindrome( nr ):

    newNr = 0
    while nr > 0:

        newNr = newNr*10 + nr%10
        nr //= 10

    return newNr


n = int(input("Please input a number :) >> "))
new = int(palindrome( n ))
print( new )
