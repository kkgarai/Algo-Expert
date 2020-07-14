"""
Boggle Board
Given a Boggle Board of characters in the form of 2-D list and a set of words to search,
we need to find words from our list which are present in our Boggle Board.
It is just like finding a word from a 2-D matrix.
The words need not be in a horizontal or vertical line.
They can also come in zig-zag manner.
"""


# O(w*s + n*m*8^s) time / O(w*s + n*m) space
# where w: no of words to search    s: length of longest word
#       n,m:dimension of board

def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    finalWords = {}
    visited = [[False for letter in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, trie.root, visited, finalWords)
    return list(finalWords.keys())


def explore(i, j, board, trieNode, visited, finalWords):
    if visited[i][j]:
        return
    letter = board[i][j]
    if letter not in trieNode:
        return
    visited[i][j] = True
    trieNode = trieNode[letter]
    if "*" in trieNode:
        finalWords[trieNode["*"]] = True
    neighbors = getNeighbors(i, j, board)
    for neighbor in neighbors:
        explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWords)
    visited[i][j] = False


def getNeighbors(i, j, board):
    neighbors = []
    if i > 0 and j > 0:
        neighbors.append([i - 1, j - 1])
    if i > 0 and j < len(board[0]) - 1:
        neighbors.append([i - 1, j + 1])
    if i < len(board) and j < len(board[0]) - 1:
        neighbors.append([i + 1, j + 1])
    if i < len(board) - 1 and j > 0:
        neighbors.append([i - 1, j - 1])
    if i > 0:
        neighbors.append([i - 1, j])
    if i < len(board[0]) - 1:
        neighbors.append([i + 1, j])
    if j > 0:
        neighbors.append([i, j - 1])
    if j < len(board[0]) - 1:
        neighbors.append([i, j + 1])
    return neighbors


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word
