"""
Sorting a list with 3 unique numbers
If we us any sorting method we may need O(nlog(n)) time.
But we need to do it in linear time
"""
def sortNums(nums):
    count={}
    for n in nums:
        count[n]=count.get(n,0)+1
    return ([1]*count.get(1,0)+
            [2]*count.get(2,0)+
            [3]*count.get(3,0))

print(sortNums([3,3,2,1,3,2,1]))
