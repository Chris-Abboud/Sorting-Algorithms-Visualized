from Algorithms import *
from UI_Functions import *
from BarClass import *
from SortingAlgorithms import *
from graphics import *


def main():
    WindowWidth = 1000

    ListInputs = ListCreationInputs()
    ValueList = GenerateList(ListInputs[0], ListInputs[1], ListInputs[2])
    VisualBars = GenerateBars(ValueList,WindowWidth, max(ValueList))

    window = GraphWin("Sorting Algorithms Visualized", WindowWidth, max(ValueList))
    window.setBackground('black')
    plotGraph(VisualBars, window)

    window.getMouse()

main()
