"""
Continuous Median
Find Median in constant time.
We keep on adding numbers to a list and continuously check the median.
eg: Numbers:            5   10  100   200  6   13     14
    Continuous Median:  5  7.5  10    55   10  11.5   13
"""



class ContinuousMedianHandler:
    def __init__(self):
        self.lowers=Heap(MAX_HEAP_FUNC,[])
        self.greater=Heap(MIN_HEAP_FUNC,[])
        self.median=None

    # O(log(N)) time / O(N) space
    def insert(self,number):
        if not self.lowers.length or number<self.lowers.peek():
            self.lowers.insert(number)
        else:
            self.greater.insert(number)

        self.rebalanceHeap()

        self.updateMedian()

    def updateMedian(self):
        if self.lowers.length==self.greater.length:
            self.median=(self.lowers.peek()+self.greater.peek())/2
        elif self.lowers.length>self.greater.length:
            self.median=self.lowers.peek()
        else:
            self.median=self.greater.peek()

    def rebalanceHeap(self):
        if self.lowers.length-self.greater.length==2:
            self.greater.insert(self.lowers.remove())
        elif self.greater.length-self.lowers.length==2:
            self.lowers.insert(self.greater.remove())

    def getMedian(self):
        return self.median

class Heap:
    def __init__(self,comparisonFuns, array):
        self.heap = self.buildHeap(array)
        self.comparisonFunc=comparisonFuns
        self.length=len(self.heap)

    # O(n) time / O(1) space
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 1) // 2
        for currentIdx in reversed(range(firstParentIdx)):
            self.shiftDown(currentIdx, len(array) - 1, array)
        return array

    # O(log(n)) time / O(1) space
    def shiftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2<=endIdx else -1
            if childTwoIdx != -1 :
                if self.comparisonFunc(heap[childTwoIdx],heap[childOneIdx]):
                    idxToSwap=childTwoIdx
                else:
                    idxToSwap=childOneIdx
            else:
                idxToSwap=childOneIdx
            if self.comparisonFunc(heap[idxToSwap],heap[currentIdx]):
                self.swap(currentIdx,idxToSwap,heap)
                currentIdx=idxToSwap
                childOneIdx=currentIdx*2+1
            else:
                return

    # O(log(n)) time / O(1) space
    def shiftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 :
            if self.comparisonFunc(heap[currentIdx],heap[parentIdx]):
                self.swap(currentIdx, parentIdx, heap)
                currentIdx = parentIdx
                parentIdx = (currentIdx - 1) // 2
            else:
                return

    # O(1) time / O(1) space
    def peek(self):
        return self.heap[0]

    # O(log(n)) time / O(1) space
    def remove(self):
        valueToRemove = self.heap.pop(0)
        self.length-=1
        self.shiftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.length+=1
        self.shiftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

def MAX_HEAP_FUNC(a,b):
    return a>b

def MIN_HEAP_FUNC(a,b):
    return a<b