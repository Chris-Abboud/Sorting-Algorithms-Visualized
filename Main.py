from Algorithms import *
from UI_Functions import *
from BarClass import *
from SortingAlgorithms import *
from graphics import *

def main():
    WindowWidth = 1000
    ButtonSpace = 100
    ButtonHeight = 80
    ListValues = 500
    ListMaximum = 500

    ListInputs = [ListValues, 1, ListMaximum] # Random List [Range, Low, High]
    ValueList = GenerateList(ListInputs[0], ListInputs[1], ListInputs[2])
    VisualBars = GenerateBars(ValueList,WindowWidth, max(ValueList)) #Transforms List to List of super class

    window = GraphWin("Sorting Algorithms Visualized", WindowWidth, max(ValueList) + ButtonHeight, autoflush=False) #Creates Window
    window.setBackground('black')
    plotGraph(VisualBars, window)
    
    while True:
        Selection, Bubble, Insertion, Merge, Quick, Reset = buttons(WindowWidth, ListInputs[2], ButtonSpace, ButtonHeight, window)
        clickPoint = window.getMouse()

        if inside(clickPoint, Selection):
            SelectionSort(VisualBars, window, max(ValueList))
        elif inside(clickPoint, Bubble):
            BubbleSort(VisualBars, window, max(ValueList))
        elif inside(clickPoint, Insertion):
            InsertionSort(VisualBars, window, max(ValueList))
        elif inside(clickPoint, Merge):
            setXValues(VisualBars, window)
        elif inside(clickPoint, Quick):
            QuickSort(VisualBars, 0, ListValues - 1, window, max(ValueList))
        elif inside(clickPoint, Reset):
            ValueList = GenerateList(ListInputs[0], ListInputs[1], ListInputs[2])
            VisualBars = GenerateBars(ValueList,WindowWidth, max(ValueList))
            clear(window)
            plotGraph(VisualBars, window)
            


main()





