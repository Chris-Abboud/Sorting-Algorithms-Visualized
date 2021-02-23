#%%
import copy
from UI_Functions import *
from graphics import *
from BarClass import *
import time

def clear(win):
    for item in win.items[:]:
        item.undraw()
    
def ShowSwap(RecOne, RecTwo, win):
    RecOne.undraw()
    RecOne.setFill("Green")
    RecOne.draw(win)

    RecTwo.undraw()
    RecTwo.setFill("Green")
    RecTwo.draw(win)

    win.update()

def setXValues(List, win):
    List2 = copy.copy(List)
    PossXs = []
    for thing in List:
        PossXs.append([thing.p1.x, thing.p2.x, thing])
        
    PossXs = sorted(PossXs, key=lambda x: x[1])
    count = 0

    for thing in List:
        thing.p1.x = PossXs[count][0]
        thing.p2.x = PossXs[count][1]
        count+=1

    return List


def SelectionSort(List2, win, WinHeight):
    for i in range(len(List2)):
        MinimumValue = List2[i]
        SwapIndex = i

        for j in range(i, len(List2)):
            if List2[j].value < MinimumValue.value:
                MinimumValue = List2[j]
                SwapIndex = j

        SwapValue = List2[i].value #Must use integer. Using object itself will cause the entire object to change the others
        List2[i].p1.y = WinHeight - MinimumValue.value #Must subtract from max height value to un-invert the rectangle
        List2[i].value = MinimumValue.value

        List2[SwapIndex].p1.y = WinHeight - SwapValue
        List2[SwapIndex].value = SwapValue

        if (SwapIndex != i):
            ShowSwap(List2[SwapIndex], List2[i], win) #Visuals Shows what happens when 2 things get swapped
            
        #time.sleep(.025)
        List2[SwapIndex].setFill("Red")
        List2[i].setFill("Red")
        win.update() #Updates Window After Any Changes

    return List2

def BubbleSort(List2, win, WinHeight):

    for i in range(len(List2) - 1):
        for j in range(0, len(List2) - i - 1):
            if List2[j].value > List2[j+1].value:
                TempForward = List2[j+1].value
                TempBack = List2[j].value

                List2[j].value = TempForward
                List2[j+1].value = TempBack

                List2[j].p1.y = WinHeight - TempForward
                List2[j+1].p1.y = WinHeight - TempBack

                ShowSwap(List2[j], List2[j+1], win)

                List2[j].setFill("Red")
                List2[j+1].setFill("Red")
                win.update()

    return List2

def InsertionSort(List, win, WindowHeight):
    List2 = copy.copy(List)

    for i in range(1, len(List2)): 
        key = List2[i].value 
        j = i-1
        while (j >=0 and key < List2[j].value): 
                List2[j+1].p1.y = WindowHeight - List2[j].value
                List2[j+1].value = List2[j].value
                ShowSwap(List2[j+1], List2[j], win)
                List2[j].setFill("Red")
                List2[j+1].setFill("Red")
                j -= 1

        
        List2[j+1].value = key 
        List2[j+1].p1.y = WindowHeight - key
        ShowSwap(List2[j+1], List2[j], win)
        List2[j].setFill("Red")
        List2[j+1].setFill("Red")
        #time.sleep(.006)

    return List2

#%% 
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

def QuickSort(List, begin, end, win, WindowHeight):
    if (begin < end):
        partitionIndex = partition(List, begin, end, WindowHeight, win)

        QuickSort(List, begin, partitionIndex-1, win, WindowHeight)
        QuickSort(List, partitionIndex+1, end, win, WindowHeight)
    

def partition(List, begin, end, WindowHeight, win):
    pivot = List[end]
    i = (begin - 1)

    for j in range(begin, end):
        if (List[j].value <= pivot.value):
            i+=1

            swapTemp = List[i].value
            List[i].value = List[j].value
            List[i].p1.y = WindowHeight - List[i].value
            List[j].value = swapTemp
            List[j].p1.y = WindowHeight - swapTemp
            ShowSwap(List[i], List[j], win)
            List[i].setFill("Red")
            List[j].setFill("Red")

    swapTemp = List[i+1].value
    List[i+1].value = List[end].value
    List[i+1].p1.y = WindowHeight - List[i+1].value
    List[end].value = swapTemp
    List[end].p1.y = WindowHeight - swapTemp
    ShowSwap(List[i+1], List[end], win)
    List[i+1].setFill("Red")
    List[end].setFill("Red")

    return i+1
    



#%%