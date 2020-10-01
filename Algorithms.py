import copy

def SelectionSort(List):
    List2 = copy.copy(List)
    for i in range(len(List2)):
        MinimumValue = List2[i]
        SwapIndex = i
        
        for j in range(i, len(List2)):
            if List2[j] < MinimumValue:
                MinimumValue = List2[j]
                SwapIndex = j

        SwapValue = List2[i]
        List2[i] = MinimumValue
        List2[SwapIndex] = SwapValue

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
    return None

def MergeSort(List):
    return None

def QuickSort(List):
    return None
