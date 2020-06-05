"""
Move Elements To End
Given an array and an integer we need to move all the instances of the integer to the  end of the array

"""


# O(n) time / O(1) space

def moveElementToend(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        while array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1


    return array


array = list(map(int, input().split()))
num = int(input())
print(moveElementToend(array,num))
