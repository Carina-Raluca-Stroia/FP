# For a given natural number n find the minimal natural number m formed with the same digits. (e.g. n=3658, m=3568).

# a function that receives a nr as a param and converts it into a list of chars so it can easily sort through the
# digits to find the min nr
def minNr( nr ):

    nrString = str(nr)
    listOfDigits = list(nrString)

    length = len(listOfDigits)

    # selection sort to sort the digits in ascending order
    for i in range(length - 1):
        for j in range( i+1, length):

            if listOfDigits[i] > listOfDigits[j]:
                aux = listOfDigits[i]
                listOfDigits[i] = listOfDigits[j]
                listOfDigits[j] = aux

    newNr = int(''.join(listOfDigits))
    return newNr


# the main program

nr = int(input("Please input a number :) >> "))
print(minNr(nr))