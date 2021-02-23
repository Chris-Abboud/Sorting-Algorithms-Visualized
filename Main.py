from Algorithms import *
from UI_Functions import *
from BarClass import *
from SortingAlgorithms import *
from graphics import *

def main():
    WindowWidth = 1000
    ButtonSpace = 100
    ButtonHeight = 80
    ListValues = 150
    ListMaximum = 500
    ConsoleSpace = 50
    text = "150"

    ListInputs = [ListValues, 1, ListMaximum] # Random List [Range, Low, High]
    ValueList = GenerateList(ListInputs[0], ListInputs[1], ListInputs[2])
    VisualBars = GenerateBars(ValueList,WindowWidth, max(ValueList)) #Transforms List to List of super class

    window = GraphWin("Sorting Algorithms Visualized - Developed by Christopher Abboud", WindowWidth, max(ValueList) + ButtonHeight + ConsoleSpace, autoflush=False) #Creates Window
    window.setBackground('black')
    plotGraph(VisualBars, window)
    Selection, Bubble, Insertion, Merge, Quick, Reset, ConsoleText, Number = buttons(WindowWidth, ListInputs[2], ButtonSpace, ButtonHeight, ConsoleSpace, text, window)
    print(Number)

    while True:
        clickPoint = window.getMouse()

        if inside(clickPoint, Selection):
            changeConsoleText(ConsoleText, "Selection Sort Working", window)
            SelectionSort(VisualBars, window, max(ValueList))
            changeConsoleText(ConsoleText, "Ready", window)
        
        elif inside(clickPoint, Bubble):
            changeConsoleText(ConsoleText, "Bubble Sort Working", window)
            BubbleSort(VisualBars, window, max(ValueList))
            changeConsoleText(ConsoleText, "Ready", window)

        elif inside(clickPoint, Insertion):
            changeConsoleText(ConsoleText, "Insertion Sort Working", window)
            InsertionSort(VisualBars, window, max(ValueList))
            changeConsoleText(ConsoleText, "Ready", window)

        elif inside(clickPoint, Merge):
            changeConsoleText(ConsoleText, "Merge Sort Working", window)
            setXValues(VisualBars, window)
            changeConsoleText(ConsoleText, "Ready", window)

        elif inside(clickPoint, Quick):
            changeConsoleText(ConsoleText, "Quick Sort Working", window)
            QuickSort(copy.copy(VisualBars), 0, int(text) - 1, window, max(ValueList))
            changeConsoleText(ConsoleText, "Ready", window)

        elif inside(clickPoint, Reset):
            text = Number.getText()
            if (not text.isdigit()):
                changeConsoleText(ConsoleText, "You must input an integer", window)
                time.sleep(1)
                changeConsoleText(ConsoleText, "Ready", window)
            elif int(text) < 1:
                changeConsoleText(ConsoleText, "Must have a minimum value of at least 1", window)
                time.sleep(1)
                changeConsoleText(ConsoleText, "Ready", window)
            elif int(text) > 500:
                changeConsoleText(ConsoleText, "Must have a maximum value of 500", window)
                time.sleep(1)
                changeConsoleText(ConsoleText, "Ready", window)
            else: 
                ValueList = GenerateList(int(text), ListInputs[1], ListInputs[2])
                VisualBars = GenerateBars(ValueList,WindowWidth, max(ValueList))
                clear(window)
                plotGraph(VisualBars, window)
                Selection, Bubble, Insertion, Merge, Quick, Reset, ConsoleText, Number = buttons(WindowWidth, ListInputs[2], ButtonSpace, ButtonHeight, ConsoleSpace, text, window)
            


main()





