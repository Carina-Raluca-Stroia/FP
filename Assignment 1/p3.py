# Generate the largest perfect number smaller than a given natural number n. If such a number does not exist, a message should be displayed. A number is perfect if it is equal to the sum of its divisors, except itself. (e.g. 6 is a perfect number, as 6=1+2+3).

# function that verifies if the given param is a perfect nr
def perfectNr( nr ):

    if nr == 1:
        return False

    sum = 0
    d = 2
    while d <= nr/2 :
        if nr % d == 0:
            sum += d
        d += 1

    sum += 1

    if sum == nr:
        return True
    return False

# function that searches for a perfect nr
def search( nr ):

    nr -= 1
    while nr > 0:
        if perfectNr( nr ):
            return nr
        nr -= 1;

    return False


# main function
n = int(input("Please enter a number :) >> "))
res = search( n )

if res != False:
    print(f"The largest perfect number smaller than {n} is {res} :) " )
else:
    print(f"There are no perfect numbers smaller than {n} :( ")