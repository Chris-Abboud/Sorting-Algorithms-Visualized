import random
import time
from Algorithms import *
from UI_Functions import *

List = []

ListLength = float(input("How many numbers do you want in your list?: "))
ListLowerRange = float(input("What is the lower range of the random list?: "))
ListUpperRange = float(input("What is the upper range of the random list?: "))

for i in range(int(ListLength)):
    List.append(random.randint(int(ListLowerRange),int(ListUpperRange)))

print("The random list is: ", List)


printMenu()

choice = int(float(input("What sorting algorithm would you like to use?", )))


time1 = time.time()
SelectionSort(List)
time2 = time.time()

print(List, "Time: ", time2 - time1)


time1 = time.time()
BubbleSort(List)
time2 = time.time()
print(List, "Time: ", time2 - time1)

