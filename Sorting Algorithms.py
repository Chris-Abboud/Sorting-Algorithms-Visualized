import time
from Algorithms import *
from UI_Functions import *

ListInputs = ListCreationInputs()
List = GenerateList(ListInputs[0], ListInputs[1], ListInputs[2])
print("The random list is: ", List)


Choice = printMenu()


print("--------------------------------------------------------------")
time1 = time.time()
SelectionSort(List)
time2 = time.time()
print("Selection Sort Time: ", time2 - time1)


time1 = time.time()
BubbleSort(List)
time2 = time.time()
print("Bubble Sort Time: ", time2 - time1)

