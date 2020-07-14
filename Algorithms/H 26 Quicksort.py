"""
Quicksort

"""


# O(nlog(n)) time / O(log(n)) space

def quickSort(array):
    quicksortHelper(array, 0, len(array) - 1)
    return array


def quicksortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1  
    rightIdx = endIdx

    while leftIdx <= rightIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(array, leftIdx, rightIdx)
            leftIdx+=1
            rightIdx-=1
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    swap(array, pivotIdx, rightIdx)
    quicksortHelper(array, startIdx, rightIdx - 1)
    quicksortHelper(array, rightIdx + 1, endIdx)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
