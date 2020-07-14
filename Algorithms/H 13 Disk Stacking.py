"""
Disk Stacking
Given a list of lists representing the dimensions of disks.
We need to find the max height possible by stacking the disks.
Note: A disk should have strictly smaller dimensions than the ones below it.

Dynamic Programming

eg: input format: [[w,d,h], [ w,d,h], ......]
                  where w: width of the disk
                        d: depth of the disk
                        h: height of the disk

   input: [[2,2,1],[2,1,2],[3,2,3],[2,3,4],[4,4,5],[2,2,8]]
   result: 2+3+5=10
   output: [[2, 1, 2], [3, 2, 3], [4, 4, 5]]
"""


# O(N^2) time / O (N) space
def diskStacking(disks):
    disks.sort(key=lambda disk: disk[2])
    heights = [disk[2] for disk in disks]
    sequences = [None for _ in disks]
    maxHeightIdx = 0
    for i in range(1, len(disks)):
        currentDisk = disks[i]
        for j in range(i):
            otherDisk = disks[j]
            if areValidDimensions(otherDisk, currentDisk):
                if heights[i] < currentDisk[2] + heights[j]:
                    heights[i] = currentDisk[2] + heights[j]
                    sequences[i] = j
        if heights[i] > heights[maxHeightIdx]:
            maxHeightIdx = i
    return buildSequence(disks, sequences, maxHeightIdx)


def areValidDimensions(o, c):
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]


def buildSequence(disks, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(disks[currentIdx])
        currentIdx = sequences[currentIdx]

    return list(reversed(sequence))
