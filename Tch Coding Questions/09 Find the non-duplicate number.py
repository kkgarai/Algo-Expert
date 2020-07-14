"""
Find the non-duplicate number
Given an array which contains duplicate numbers.
All the numbers have duplicate entries except one , we need to find that "one" number.

We use the XOR operation to do it.
"""


class Solution:
    # Using Dictionary
    def singleNummber(self,nums):
        occurence={}
        for n in nums:
            occurence[n]=occurence.get(n,0)+1

        for key,value in occurence.items():
            if value==1:
                return key

    # using XOR operator
    def singleNumber2(self,nums):
        unique=0
        for n in nums:
            unique ^=n
        return unique



print(Solution().singleNummber([4,3,2,1,4,3,2,4,5,5,3]))
print(Solution().singleNumber2([5,4,6,5,3,6,8,3,8,9,9]))