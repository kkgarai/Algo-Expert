"""
Min Heap Construction
In a min heap every node's value is less or equal to its children's value.
Steps: Build Heap
       Shift Down
       Shift Up
       Insert
       Remove

Index: Current Node: i
       Left Child: 2*i + 1
       Right Child: 2*i + 2

       if child node is at i, parent node is at floor((i-1)/2)
"""


class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    # O(n) time / O(1) space
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx)):
            self.shiftDown(currentIdx, len(array) - 1, array)
        return array

    # O(log(n)) time / O(1) space
    def shiftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 1 else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                break

    # O(log(n)) time / O(1) space
    def shiftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    # O(1) time / O(1) space
    def peek(self):
        return self.heap[0]

    # O(log(n)) time / O(1) space
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.shiftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.shiftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
