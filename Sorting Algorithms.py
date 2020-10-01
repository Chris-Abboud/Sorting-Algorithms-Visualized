import random
import time

List = []

ListLength = float(input("How many numbers do you want in your list?: "))
ListLowerRange = float(input("What is the lower range of the random list?: "))
ListUpperRange = float(input("What is the upper range of the random list?: "))

for i in range(int(ListLength)):
    List.append(random.randint(int(ListLowerRange),int(ListUpperRange)))

print("The random list is: ", List)


def printMenu():
    print()
    print("1. Selection Sort")
    print("2. Bubble Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print()


'''
Selection sort will look for the lowest value, and swap the indexes. Then offsets by 1 and continues.
[4,6,7,1]
[1,6,7,4]
[1,4,7,6]
[1.4.6.7]

'''
def SelectionSort(List):
    for i in range(int(ListLength)):
        MinimumValue = List[i]
        SwapIndex = i
        
        for j in range(i, int(ListLength)):
            if List[j] < MinimumValue:
                MinimumValue = List[j]
                SwapIndex = j

        SwapValue = List[i]
        List[i] = MinimumValue
        List[SwapIndex] = SwapValue

    return List

def BubbleSort(List):
    
    for i in range(int(ListLength) - 1):
        for j in range(0, int(ListLength) - i - 1):
            if List[j] > List[j+1]:
                Minimum = List[j+1]
                Maximum = List[j]
                List[j] = Minimum
                List[j+1] = Maximum
    
    return List

printMenu()

choice = int(float(input("What sorting algorithm would you like to use?", )))

if (choice == 1):
    time1 = time.time()
    SelectionSort(List)
    time2 = time.time()

    print(List, "Time: ", time1 - time2)

def InsertionSort(List):
    return None

def MergeSort(List):
    return None

def QuickSort(List):
    return None

# %%
