import random

def ListCreationInputs():
    ListLength = float(input("How many numbers do you want in your list?: "))
    ListLowerRange = float(input("What is the lower range of the random list?: "))
    ListUpperRange = float(input("What is the upper range of the random list?: "))
    return [ListLength, ListLowerRange, ListUpperRange]
    
def printMenu():
    print()
    print("1. Selection Sort")
    print("2. Bubble Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print()

    return int(float(input("What sorting algorithm would you like to use? ", )))

def GenerateList(ListLength, ListLowerRange, ListUpperRange):
    List = []
    for i in range(int(ListLength)):
        List.append(random.randint(int(ListLowerRange),int(ListUpperRange)))
    return List