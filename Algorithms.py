#%%
import copy
from UI_Functions import *
from graphics import *

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def SelectionSort(List, win):
    List2 = copy.copy(List)
    for i in range(len(List2)):
        MinimumValue = List2[i]
        SwapIndex = i
        print("I", i)

        for j in range(i, len(List2)):
            if List2[j] < MinimumValue:
                MinimumValue = List2[j]
                SwapIndex = j

        SwapValue = List2[i]
        List2[i] = MinimumValue
        List2[SwapIndex] = SwapValue

        clear(win)
        plotGraph(List2, win)

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

def plotGraph(List, win):

    RectLength = 1000 / len(List)


    for i in range(len(List)):
        #print("I:", i)
        #print("Point 1: ", i * RectLength, List[i])
        #print("Point 2: ", i * RectLength + RectLength, 1000)
        rect = Rectangle(Point(i * RectLength, Height - List[i]), Point(i * RectLength + RectLength, 1000))
        rect.setOutline("")
        rect.setFill('red')
        rect.draw(win)

    



List = GenerateList(200, 0, 500)
Length = 1000
Height = max(List)
win = GraphWin("My Window", Length, Height)
win.setBackground('black')
SelectionSort(List, win)

win.getMouse()

#%%