import time
from Algorithms import *
from UI_Functions import *

def temp():
    ListInputs = ListCreationInputs()
    List = GenerateList(ListInputs[0], ListInputs[1], ListInputs[2])

    while True:
        Choice = printMenu()

        if Choice == 1 or Choice == 6:
            print("--------------------------------------------------------------")
            time1 = time.time()
            SelectionSort(List)
            time2 = time.time()
            print("Selection Sort Time: ", time2 - time1)

        if Choice == 2 or Choice == 6:
            time1 = time.time()
            BubbleSort(List)
            time2 = time.time()
            print("Bubble Sort Time: ", time2 - time1)

        if Choice == 3 or Choice == 6:
            time1 = time.time()
            InsertionSort(List)
            time2 = time.time()
            print("Insertion Sort Time: ", time2 - time1)

        if Choice == 4 or Choice == 6:
            time1 = time.time()
            MergeSort(List)
            time2 = time.time()
            print("Merge Sort Time: ", time2 - time1)

        if Choice == 5 or Choice == 6:
            time1 = time.time()
            QuickSort(List)
            time2 = time.time()
            print("QuickSort Time: ", time2 - time1)

        if Choice == 7:
            break

    print("Thank you for trying this out!")