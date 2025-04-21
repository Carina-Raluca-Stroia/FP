import random
def randomList(size):
    # generates list of 'nr' random nrs between 0 -> 1000

    arr = [random.randint(0, 1000) for _ in range(size)]
    return arr


# Interpolation search - linear
# faster than binary search if the nr are uniformly distributed in the list
def interpolationSearch(list, valueToSearch, left, right):
    # the list of nr has to be sorted
    # estimates the position of the search key ( aka pos ) based on its value
    if left <= right and valueToSearch >= list[left] and valueToSearch <= list[right]:

        # if there is only one elem or all elems are equal
        if left == right or list[left] == list[right]:
            if list[left] == valueToSearch:
                return left
            else:
                return -1

        # computing the position of the val
        position = int(left + float(right - left) / (list[right] - list[left]) * (valueToSearch - list[left]))

        # the val is found at position 'pos'
        if list[position] == valueToSearch:
            return position

        # searching the right subarray if the val is bigger than where we 'landed'
        elif list[position] < valueToSearch:
            return interpolationSearch(list, valueToSearch, position + 1, right)

        # searching the left subarray if the val is lower than where we 'landed'
        else:
            return interpolationSearch(list, valueToSearch, left, position - 1)

    return -1

# for Bogo sort
def shuffle(list):
    # shuffling the array

    for index in range(len(list)):
        random_index = random.randint(0, len(list) - 1)
        # swapping the values chosen randomly
        list[index], list[random_index] = list[random_index], list[index]


def listSorted(list):
    # checks if the array is sorted ( ascending order )
    for index in range(len(list) - 1):
        if list[index] > list[index + 1]:
            return False
    return True

def bogoSort(list, step):
    # Bogo sort randomly shuffles the list until it's sorted ( very inefficient )
    stepCount = 0
    while not listSorted(list):
        stepCount += 1
        if step == stepCount:
            print(list)
            stepCount = 0
        shuffle(list)
    return list


# Gnome Sort: like insertion sort, but swaps adjacent elements like a gnome
def gnomeSort(list, step):
    # Gnome sort moves back and forth like a gnome until the list is sorted
    stepCount = 0  # to keep track of steps
    position = 0
    while position < len(list):

        stepCount += 1
        if step == stepCount:
            print(list)
            stepCount = 0

        # jumping over the first pos
        if position == 0:
            position += 1


        if list[position] >= list[position - 1]:
            position += 1
        else:
            list[position], list[position - 1] = list[position - 1], list[position]
            position -= 1

    return list


def main():
    listExists = False
    listSorted = False
    list = []

    generateListRandom = "1"
    interpolationSearchOption = "2"
    BogoSortOption = "3"
    GnomeSortOption = "4"
    printListOption = "5"
    exitOption = "0"


    while True:
        print("\n         ------ Search & sort ------\n"
              "     1. Generate a list of random numbers.\n"
              "     2. Search for a number using interpolation search.\n"
              "     3. Sort the list using Bogo sort.\n"
              "     4. Sort the list using Gnome sort.\n"
              "     5. Print the list.\n"
              "     0. Exit :(\n");

        command = int(input(" Please enter your choice >> "))

        if command == exitOption:
            print("Bye bye :(")
            break

        elif command == generateListRandom:
            # generate a random list of numbers
            listExists = True
            listSorted = False

            size = int(input(" -- How many elements in the list? >> "))
            list = randomList(size)
            print(list)



        elif command == interpolationSearchOption:
            # search for a number using interpolation search
            if not listExists:
                print(" ! Please generate a random list of numbers first and then try again ( see 1.) ! \n")
            elif not listSorted:
                print(" ! Please sort the list before searching ( see 3. or 4. ) !\n")
            else:
                valueToSearch = int(input(" -- What number are you looking for? >>  "))
                valueFound = interpolationSearch(list, valueToSearch, 0, len(list) - 1)

                if valueFound == -1:
                    print(f"The value {valueToSearch} is not in the list :( ")
                else:
                    print(f" The value is in the list on position {valueFound} ")



        elif command == BogoSortOption:
            # sort the list using Bogo sort
            if not listExists:
                print(" ! Please generate a random list of numbers first and then try again ( see 1.) ! \n")
            else:
                step = int(input(" -- Please enter the step >>  "))
                list = bogoSort(list, step)
                print(str(list) + "\n")
                listSorted = True



        elif command == GnomeSortOption:
            # sort the list using Gnome sort
            if not listExists:
                print(" ! Please generate a random list of numbers first and then try again ( see 1.) ! \n")
            else:
                step = int(input(" --  Please enter the step >>  "))
                list = gnomeSort(list, step)
                print(str(list) + "\n")
                listSorted = True

        elif command == printListOption:

            print(list)
            print("\n")


main()
