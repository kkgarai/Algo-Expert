"""
Longest Substring Wthout Duplication
eg: Input: clementisacap
    Output:mentisac
"""


# O(N) time / O(min(N,A)) space where A: no of unique characters in the string
def longestSubstringWthoutDuplication(string):
    lastSeen={}
    longest=[0,1]
    startIdx=0
    for i,char in enumerate(string):
        if char in lastSeen:
            startIdx=min(startIdx,lastSeen[char]+1)
        if longest[1]-longest[0]<i+1-startIdx:
            longest=[startIdx,i+1]
        lastSeen[char]=i
    return string[longest[0]:longest[1]]