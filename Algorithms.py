#%%
import copy
from graphics import *
import time

def clear(win):
    for item in win.items[:]:
        item.undraw()
def isAlreadySorted(List):
    for i in range(1, len(List)):
        if (List[i].value < List[i-1].value):
            return False
    return True
    
def ShowSwap(RecOne, RecTwo, win):
    RecOne.undraw()
    RecOne.setFill("Green")
    RecOne.draw(win)

    RecTwo.undraw()
    RecTwo.setFill("Green")
    RecTwo.draw(win)

    win.update()

    RecOne.setFill("Red")
    RecTwo.setFill("Red")

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

        SwapValue = List2[i].value #Must use integer. Using object itself will just create pointer
        List2[i].p1.y = WinHeight - MinimumValue.value #Must subtract from max height value to un-invert the rectangle
        List2[i].value = MinimumValue.value

        List2[SwapIndex].p1.y = WinHeight - SwapValue
        List2[SwapIndex].value = SwapValue

        if (SwapIndex != i):
            ShowSwap(List2[SwapIndex], List2[i], win) #Visuals Shows what happens when 2 things get swapped
            
        #time.sleep(.025)

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

                j -= 1

        
        List2[j+1].value = key 
        List2[j+1].p1.y = WindowHeight - key
        ShowSwap(List2[j+1], List2[j], win)

        #time.sleep(.006)

    return List2

#%% 
def merge(arr, start, mid, end, win, WindowHeight): # IN-PLACE Merge sort - No extra array is created
    start2 = mid + 1

    while (start <= mid and start2 <= end):
        if (arr[start].value <= arr[start2].value):
            start += 1
        else:
            value = arr[start2].value
            index = start2
            while (index != start):
                arr[index].value = arr[index - 1].value
                arr[index].p1.y = WindowHeight - arr[index].value
                ShowSwap(arr[index], arr[index-1], win)

                index -= 1
             
            arr[start].value = value
            arr[start].p1.y = WindowHeight - arr[start].value
            ShowSwap(arr[index], arr[start], win)

            start += 1
            mid += 1
            start2 += 1
         
def mergeSort(arr, left, right, win, WindowHeight):
    if (left < right):
        middle = left + (right - left) // 2
        mergeSort(arr, left, middle, win, WindowHeight)
        mergeSort(arr, middle + 1, right, win, WindowHeight)
        merge(arr, left, middle, right, win, WindowHeight)

#%%
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


    swapTemp = List[i+1].value
    List[i+1].value = List[end].value
    List[i+1].p1.y = WindowHeight - List[i+1].value
    List[end].value = swapTemp
    List[end].p1.y = WindowHeight - swapTemp
    ShowSwap(List[i+1], List[end], win)


    return i+1

#%%