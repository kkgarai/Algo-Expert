"""
Longest Sequence with two Unique Numbers
Given an array we need to find the longest Longest Sequence with exactly two Unique Numbers.

eg: array: [1,3,5,3,1,3,1,5]
    Longest Sequence with two Unique Numbers: [3,1,3,1]
"""


def findSequence(seq):
    if len(seq)<2:
        return len(seq)

    a,b=seq[0],seq[1]

    last_num=b
    last_num_count=(a==b)
    length=1
    max_length=1

    for n in seq[1:]:
        if n in (a,b):
            length+=1
            if b==n:
                last_num_count+=1
            else:
                last_num=a
                last_num_count=1
        else:
            a=last_num
            b=n
            last_num=b
            length=last_num_count+1
        max_length=max(length,max_length)
    return max_length



print(findSequence([1,3,5,3,1,3,1,5]))