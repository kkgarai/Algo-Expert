"""
Min Number Of Coins For Change
we are given a target amount and unlimited coins of a given few denominatons,
we need to return the minimum number of coins to make the change

Dynamic Programming

if denom <= amount:
    nums[amount] = min { nums[amount],
                        1+nums[amount-denom]}

"""


# O(n*d) time / O(n) space
def minNumberOfCoinsForChange(n, denoms):
    """
    :param n: target amount
    :param denoms: denominations of coins available
    :return: min number of coins
    """
    numOfCoins = [float('inf') for amt in range(n + 1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(n + 1):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount], 1 + numOfCoins[amount - denom])
    return numOfCoins[n] if numOfCoins[n] != float('inf') else -1
