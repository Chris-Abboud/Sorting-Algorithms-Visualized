from Algorithms import *
from UI_Functions import *
from BarClass import *
from SortingAlgorithms import *
from graphics import *


WindowWidth = 1000
ButtonHeight = 100

ListInputs = ListCreationInputs() # Random List [Range, Low, High]
ValueList = GenerateList(ListInputs[0], ListInputs[1], ListInputs[2])
VisualBars = GenerateBars(ValueList,WindowWidth, max(ValueList)) #Transforms List to List of super class

window = GraphWin("Sorting Algorithms Visualized", WindowWidth, max(ValueList) + ButtonHeight, autoflush=False) #Creates Window
window.setBackground('black')
plotGraph(VisualBars, window)
SelectionSort(VisualBars, window)
window.getMouse()


