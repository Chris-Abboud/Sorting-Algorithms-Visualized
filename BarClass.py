from graphics import *
from UI_Functions import *
from graphics import Rectangle as RectangleBase

class MegaRect(RectangleBase): #A superclass had to be created to hold "Value" and initial Color
    color = "Red"
    value = 0

def changeConsoleText(Text, Status, window):
    Text.undraw()
    Text.setText(Status)
    Text.draw(window)
    window.update()

def GenerateBars(List, WinWidth, WinHeight): #Converts a list of values to rectangle objects used for plotting
    BarList = []
    RectLength = WinWidth / len(List)

    for i in range(len(List)):
        rect = MegaRect(Point(i * RectLength, WinHeight - List[i]), Point(i * RectLength + RectLength, WinHeight))
        rect.setFill(rect.color)
        rect.setOutline("")
        rect.value = List[i]
        BarList.append(rect)

    return BarList

def plotGraph(List, win): #Plot all bars in list
    for i in range(len(List)):
        List[i].draw(win)
    win.update()

def plotSingle(Rect, win): #Plot single bar
    Rect.draw(win)
    win.update()


def buttons(WindowWidth, WindowHeight, ButtonSpace, ButtonHeight, ConsoleSpace, text, window): #All UI Elements
    EdgeSpace = 50
    Between = 15
    Buttons = 6

    FreeSpace = WindowWidth - (EdgeSpace * 2) - (Between * Buttons)
    Spacer = FreeSpace / Buttons

    Selection = Rectangle(Point(EdgeSpace + Between, (ButtonSpace - ButtonHeight) / 2 + WindowHeight), Point(EdgeSpace + Spacer, WindowHeight + ButtonHeight - (ButtonSpace - ButtonHeight)/2))
    Selection.setFill("Orange")
    Selection.draw(window)
    SelectionCenter = Selection.getCenter()
    SelectionText = Text(SelectionCenter, "Selection Sort")
    SelectionText.draw(window)

    Bubble = Rectangle(Point(EdgeSpace + Spacer * 1 + Between * 2, (ButtonSpace - ButtonHeight) / 2 + WindowHeight), Point(EdgeSpace + Spacer * 2 + Between * 1, WindowHeight + ButtonHeight - (ButtonSpace - ButtonHeight)/2))
    Bubble.setFill("Orange")
    Bubble.draw(window)
    BubbleCenter = Bubble.getCenter()
    BubbleText = Text(BubbleCenter, "Bubble Sort")
    BubbleText.draw(window)

    Insertion = Rectangle(Point(EdgeSpace + Spacer * 2 + Between * 3, (ButtonSpace - ButtonHeight) / 2 + WindowHeight), Point(EdgeSpace + Spacer * 3 + Between * 2, WindowHeight + ButtonHeight - (ButtonSpace - ButtonHeight)/2))
    Insertion.setFill("Orange")
    Insertion.draw(window)
    InsertionCenter = Insertion.getCenter()
    InsertionText = Text(InsertionCenter, "Insertion Sort")
    InsertionText.draw(window)

    Merge = Rectangle(Point(EdgeSpace + Spacer * 3 + Between * 4, (ButtonSpace - ButtonHeight) / 2 + WindowHeight), Point(EdgeSpace + Spacer * 4 + Between * 3, WindowHeight + ButtonHeight - (ButtonSpace - ButtonHeight)/2))
    Merge.setFill("Orange")
    Merge.draw(window)
    MergeCenter = Merge.getCenter()
    MergeText = Text(MergeCenter, "Merge Sort")
    MergeText.draw(window)

    Quick = Rectangle(Point(EdgeSpace + Spacer * 4 + Between * 5, (ButtonSpace - ButtonHeight) / 2 + WindowHeight), Point(EdgeSpace + Spacer * 5 + Between * 4, WindowHeight + ButtonHeight - (ButtonSpace - ButtonHeight)/2))
    Quick.setFill("Orange")
    Quick.draw(window)
    QuickCenter = Quick.getCenter()
    QuickText = Text(QuickCenter, "Quick Sort")
    QuickText.draw(window)

    NewData = Rectangle(Point(EdgeSpace + Spacer * 5 + Between * 6, (ButtonSpace - ButtonHeight) / 2 + WindowHeight), Point(EdgeSpace + Spacer * 6 + Between * 5, WindowHeight + ButtonHeight - (ButtonSpace - ButtonHeight)/2))
    NewData.setFill("Orange")
    NewData.draw(window)
    NewDataCenter = NewData.getCenter()
    NewDataText = Text(NewDataCenter, "New Data")
    NewDataText.draw(window)

    ConsoleBox = Rectangle(Point(EdgeSpace + Between, WindowHeight + ButtonHeight - (ButtonSpace - ButtonHeight)/2 + Between), Point(EdgeSpace + Spacer, WindowHeight + ButtonHeight - (ButtonSpace - ButtonHeight)/2 + Between + Between + Between))
    ConsoleBox.setFill("Orange")
    ConsoleBox.draw(window)
    ConsoleBoxCenter = ConsoleBox.getCenter()
    ConsoleBoxText = Text(ConsoleBoxCenter, "Status: ")
    ConsoleBoxText.draw(window)

    Console = Rectangle(Point(EdgeSpace + Spacer * 1 + Between * 2, WindowHeight + ButtonHeight - (ButtonSpace - ButtonHeight)/2 + Between), Point(EdgeSpace + Spacer * 4 + Between * 3, WindowHeight + ButtonHeight - (ButtonSpace - ButtonHeight)/2 + Between + Between + Between))
    Console.setOutline("Orange")
    Console.draw(window)
    ConsoleCenter = Console.getCenter()
    ConsoleText = Text(ConsoleCenter, "Ready")
    ConsoleText.setStyle("italic")
    
    ConsoleText.setTextColor("Orange")
    ConsoleText.draw(window)

    EntryBox = Rectangle(Point(EdgeSpace + Spacer * 4 + Between * 5, WindowHeight + ButtonHeight - (ButtonSpace - ButtonHeight)/2 + Between), Point(EdgeSpace + Spacer * 5 + Between * 4, WindowHeight + ButtonHeight - (ButtonSpace - ButtonHeight)/2 + Between + Between + Between))
    EntryBox.setFill("Orange")
    EntryBox.draw(window)
    EntryBoxCenter = EntryBox.getCenter()
    EntryBoxText = Text(EntryBoxCenter, "# Of Bars:")
    EntryBoxText.draw(window)

    EntryBoxNumber = Rectangle(Point(EdgeSpace + Spacer * 5 + Between * 6, WindowHeight + ButtonHeight - (ButtonSpace - ButtonHeight)/2 + Between), Point(EdgeSpace + Spacer * 6 + Between * 5, WindowHeight + ButtonHeight - (ButtonSpace - ButtonHeight)/2 + Between + Between + Between))
    EntryBoxNumber.setFill("Orange")
    EntryBoxNumberCenter = EntryBoxNumber.getCenter()
    Number = Entry(EntryBoxNumberCenter, 12)
    Number.setFill("Black")
    Number.setTextColor("Orange")
    Number.setText(text)
    Number.draw(window)



    window.update()

    return Selection, Bubble, Insertion, Merge, Quick, NewData, ConsoleText, Number

def inside(point, rectangle): #Used for the buttons
    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()