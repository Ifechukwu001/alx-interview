#!/usr/bin/python3
"""Module containing function that check coins needed to make change"""


def makeChange(coins, total):
    """Checks nuber of coins needed to make total
    Returns:
        int: Coins count
    """
    count = 0
    tot = total
    coin_list = coins

    if total <= 0:
        return 0

    while tot:
        if len(coin_list) == 0:
            return -1
        largest = max(coin_list)
        if largest > tot:
            coin_list.remove(largest)
        else:
            count += 1
            tot -= largest
    return count
