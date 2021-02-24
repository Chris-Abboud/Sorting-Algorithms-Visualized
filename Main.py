from Algorithms import *
from UI_Functions import *
from BarClass import *
from SortingAlgorithms import *
from graphics import *

def main():
    WindowWidth = 1000 # Width of Window
    ButtonSpace = 100 # Space under window for buttons
    ButtonHeight = 80 # Height of each button
    ListValues = 150 # How many bars are initially present
    ListMaximum = 500 # Maximum height of a given bar
    ConsoleSpace = 50 # Space under buttons for the console
    text = str(ListValues) #Initial text in Entry Box

    ListInputs = [ListValues, 1, ListMaximum] # Random List [Range, Low, High]
    ValueList = GenerateList(ListInputs[0], ListInputs[1], ListInputs[2]) #A Random lies of values first has to be generated
    VisualBars = GenerateBars(ValueList,WindowWidth, max(ValueList)) #Transforms List to List of super class

    window = GraphWin("Sorting Algorithms Visualized - Developed by Christopher Abboud", WindowWidth, max(ValueList) + ButtonHeight + ConsoleSpace, autoflush=False) #Creates Window
    window.setBackground('black')
    plotGraph(VisualBars, window)
    Selection, Bubble, Insertion, Merge, Quick, Reset, ConsoleText, Number = buttons(WindowWidth, ListInputs[2], ButtonSpace, ButtonHeight, ConsoleSpace, text, window) #Creates All UI Elements

    while True:
        clickPoint = window.getMouse() # Waits for user action. Loop always running unless "X" is clicked top right.

        if inside(clickPoint, Selection) and not(isAlreadySorted(VisualBars)): #Selection Sort Double checks to make sure a sorted list doesn't go through sorting algos
            changeConsoleText(ConsoleText, "Selection Sort Working", window)
            SelectionSort(VisualBars, window, max(ValueList))
            changeConsoleText(ConsoleText, "Ready", window)
        
        elif inside(clickPoint, Bubble) and not(isAlreadySorted(VisualBars)): # Bubble Sort
            changeConsoleText(ConsoleText, "Bubble Sort Working", window)
            BubbleSort(VisualBars, window, max(ValueList))
            changeConsoleText(ConsoleText, "Ready", window)

        elif inside(clickPoint, Insertion) and not(isAlreadySorted(VisualBars)): # Insertion Sort
            changeConsoleText(ConsoleText, "Insertion Sort Working", window)
            InsertionSort(VisualBars, window, max(ValueList))
            changeConsoleText(ConsoleText, "Ready", window)

        elif inside(clickPoint, Merge) and not(isAlreadySorted(VisualBars)): # Merge Sort
            changeConsoleText(ConsoleText, "Merge Sort Working", window)
            mergeSort(VisualBars, 0, int(text) - 1, window, max(ValueList))
            changeConsoleText(ConsoleText, "Ready", window)

        elif inside(clickPoint, Quick) and not(isAlreadySorted(VisualBars)): # Quick Sort
            changeConsoleText(ConsoleText, "Quick Sort Working", window)
            QuickSort(copy.copy(VisualBars), 0, int(text) - 1, window, max(ValueList))
            changeConsoleText(ConsoleText, "Ready", window)

        elif inside(clickPoint, Reset): #Generate New Bars
            text = Number.getText() #Gets number from input box
            if (not text.isdigit()): #Checks that it is an integer
                changeConsoleText(ConsoleText, "You must input a positive integer", window)
                time.sleep(1.5)
                changeConsoleText(ConsoleText, "Ready", window)
            elif int(text) < 1: #Checks for minimum of 1
                changeConsoleText(ConsoleText, "Must have a minimum value of at least 1", window)
                time.sleep(1.5)
                changeConsoleText(ConsoleText, "Ready", window)
            elif int(text) > 500: #Checks for maximum of 500
                changeConsoleText(ConsoleText, "Must have a maximum value of 500", window)
                time.sleep(1.5)
                changeConsoleText(ConsoleText, "Ready", window)
            else: #If gets this far, then valid input
                ValueList = GenerateList(int(text), ListInputs[1], ListInputs[2]) #Generate List
                VisualBars = GenerateBars(ValueList,WindowWidth, max(ValueList)) #Convert List to Bars
                clear(window) #Clears Window
                plotGraph(VisualBars, window) #Plots Bar
                Selection, Bubble, Insertion, Merge, Quick, Reset, ConsoleText, Number = buttons(WindowWidth, ListInputs[2], ButtonSpace, ButtonHeight, ConsoleSpace, text, window) #Refresh UI Elements
            

main()





