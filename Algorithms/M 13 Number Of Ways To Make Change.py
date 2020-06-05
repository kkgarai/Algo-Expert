"""
Number Of Ways To Make Change
we are given an amount and unlimited coins of a given few denominatons,
we need to find the number of ways change can be made using these coins

Dynamic Programming

if denom<=amount:
    ways[amount]+=ways[amount-denom]

"""


# O(n*d) time / O(n) space
def noOfWaysToMakeChange(n,denoms):
    """
    :param n: targetted amount
    :param denoms: array of the available denominations
    :return: no of ways
    """
    ways=[0 for amount in range(n+1)]
    ways[0]=1

    for denom in denoms:
        for amount in range(1,n+1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]


















