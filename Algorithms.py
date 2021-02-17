#%%
import copy
from UI_Functions import *
from graphics import *
from BarClass import *
import time

def clear(win):
    for item in win.items[:]:
        item.undraw()
    

def SelectionSort(List2, win):
    for i in range(len(List2)):
        MinimumValue = List2[i]
        SwapIndex = i

        for j in range(i, len(List2)):
            if List2[j].value < MinimumValue.value:
                MinimumValue = List2[j]
                SwapIndex = j

        SwapValue = List2[i].value #Must use integer. Using object itself will cause the entire object to change the others
        

        List2[i].p1.y = MinimumValue.value
        List2[i].value = MinimumValue.value

        List2[SwapIndex].p1.y = SwapValue
        List2[SwapIndex].value = SwapValue

        if (SwapIndex != i):
            List2[SwapIndex].undraw()
            List2[i].undraw()
            List2[SwapIndex].setFill("Green")
            List2[SwapIndex].draw(win)
            List2[i].setFill("Green")
            List2[i].draw(win)
        else:
            List2[i].setFill("Green")
            List2[i].undraw()
            List2[i].draw(win)

        update()
        time.sleep(.025)
        List2[SwapIndex].setFill("Red")
        List2[i].setFill("Red")

    return List2

def BubbleSort(List):
    List2 = copy.copy(List)
    for i in range(len(List2) - 1):
        for j in range(0, len(List2) - i - 1):
            if List2[j] > List2[j+1]:
                Minimum = List2[j+1]
                Maximum = List2[j]
                List2[j] = Minimum
                List2[j+1] = Maximum
    
    return List2

def InsertionSort(List):
    List2 = copy.copy(List)
    for i in range(1, len(List2)):
        Num = List2[i]
        j = i - 1 
        while (j >= 0 and List2[j] > Num):
            List2[j+1] = List2[j]
            j-=1
        List2[j] = Num
    return List2
    
def MergeSort(List):
    List2 = copy.copy(List)
    if len(List2) <=1:
        return List2

    midpoint = int(len(List2) / 2)
    left, right = MergeSort(List2[:midpoint]), MergeSort(List2[midpoint:])
    return Merge(left, right)
    
def Merge(left, right):
    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer+=1
        else:
            result.append(right[right_pointer])
            right_pointer+=1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result

def QuickSort(List):
    List2 = copy.copy(List)
    length = len(List2)
    if length <= 1:
        return List2
    else:
        pivot = List2.pop()

    items_greater = []
    items_lower = []
    for item in List2:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return QuickSort(items_lower) + [pivot] + QuickSort(items_greater)



#%%