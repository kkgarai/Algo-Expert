"""
Multi String Search
Given a large string a list of smaller strings,
we need to check which of the smaller strings are present in the laerger string.

eg: String: this is a big string
    Search: [this,yo,is,a,bigger,string,kappa]
    Result: [T, F,  T,  T,  F,  T,  F]
"""


# O(bns) time / O(n) space
# where b: length of the bigger string
#       n: no. of smaller strings
#       s: size of the lonngest smaller string
