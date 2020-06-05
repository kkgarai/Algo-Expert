"""
Longest Peak
Given an array of heights we need to find out the length of the longest  peak.
A peak is considered when the sequence strictly increases ,reaches a maximum and then strictly decreases.

"""

def longestPeak(array):
    """
    first we find all the capable peaks and then find out the longest among them
    """
    peaks=[]
    for i in range(1,len(array)-1):
        if array[i-1]<array[i] and array[i+1]<array[i]:
            peaks.append(i)

    longestPeakLength=0
    for peak in peaks:
        left=peak-1
        right=peak+1
        while left>0 and array[left-1]<array[left]:
            left-=1
        while right<len(array)-1 and array[right]>array[right+1]:
            right+=1

        currentPeakLength=right-left+1
        if currentPeakLength>longestPeakLength:
            longestPeakLength=currentPeakLength

    return longestPeakLength



array=list(map(int,input().split()))
print(longestPeak(array))