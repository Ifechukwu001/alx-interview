#!/usr/bin/python3
"""Module containing the pascal triangle generator

"""


def _pascal_helper(array, current, stop):
    """ Recursive pascal helper

    Args:
        array (list): List containing the total output lists.
        current (int): Current iteration of the triangle.
        stop (int): the last iteration of the triangle.

    Return:
        None: Once completed.
        _pascal_helper (Function): If the iterations are not done.

    """
    if current == 1:
        array.append([1])
    elif current == 2:
        array.append([1, 1])
    else:
        last_arr = array[-1]
        last_len = len(last_arr)
        curr_arr = []
        i = 0
        j = 1
        curr_arr.append(1)
        while j < last_len:
            tmp = last_arr[i] + last_arr[j]
            i = j
            j += 1
            curr_arr.append(tmp)
        curr_arr.append(1)

        array.append(curr_arr)
    if current == stop:
        return
    else:
        return _pascal_helper(array, current + 1, stop)


def pascal_triangle(n):
    """ Pascal triangle generator

    Args:
        n (int): Number of iterations of the triangle.

    Return:
        list of lists: A list containing the triangle matrix.

    """
    if n <= 0:
        return []
    else:
        arr = []
        _pascal_helper(arr, 1, n)
        return arr
