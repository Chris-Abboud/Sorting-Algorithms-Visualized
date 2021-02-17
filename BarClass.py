from graphics import *
from UI_Functions import *
from graphics import Rectangle as RectangleBase

class MegaRect(RectangleBase):
    color = "Red"
    value = 0


def GenerateBars(List, WinWidth, WinHeight):
    BarList = []
    RectLength = WinWidth / len(List)

    for i in range(len(List)):
        rect = MegaRect(Point(i * RectLength, WinHeight - List[i]), Point(i * RectLength + RectLength, WinHeight))
        rect.setFill(rect.color)
        rect.setOutline("")
        rect.value = List[i]
        BarList.append(rect)

    return BarList

def plotGraph(List, win):
    for i in range(len(List)):
        List[i].draw(win)
    win.update()

def plotSingle(Rect, win):
    Rect.draw(win)
    win.update()
