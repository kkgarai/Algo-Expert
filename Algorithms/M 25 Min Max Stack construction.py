"""
Min Max Stack construction

        5   7   2
min :   5   7   2
max :   5   7   7
peek:   5   7   2

In a Min Max Stack we can peek ,pop,push and get the min and max value at constant time.

"""


# O(1) time / O(3*n) space

class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    # O(1) time / O(1) space
    def peek(self):
        return self.stack[len(self.stack) - 1]

    # O(1) time / O(1) space
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    # O(1) time / O(1) space
    def push(self, number):
        newMinMax = {'min': number, 'max': number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax['min'] = min(lastMinMax['min'], number)
            newMinMax['max'] = max(lastMinMax['max'], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    # O(1) time / O(1) space
    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]['min']

    # O(1) time / O(1) space
    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]['max']
