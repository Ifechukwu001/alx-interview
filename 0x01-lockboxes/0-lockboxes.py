#!/usr/bin/python3
"""Module containing the algorithm for lockboxes.

The Algorithm has a time complexity of O(n)
"""


def openBox(boxes: list[list[int]], box: int, key_list: list[int]) -> bool:
    """Opens a box
    
    Args:
        boxes (list of list of int): Box list.
        box (int): Box number.
        key_list (list of int): List of box keys.

    Returns:
        bool: True if opened , False otherwise
    """
    if box in key_list:
        key_list.extend(boxes[box])
        return True
    return False


def canUnlockAll(boxes: list[list[int]]) -> bool:
    """Can Unlock All
    
    Args:
        boxes (list of list of int): Box list.
        
    Returns:
        bool: True if possible, False otherwise.
    """
    opened_list: list[int] = []
    closed_list: list[int] = []
    key_list: list[int] = [0]

    for box in range(len(boxes)):
        if openBox(boxes, box, key_list):
            opened_list.append(box)
        else:
            closed_list.append(box)

    if closed_list:
        for box in closed_list.copy():
            if openBox(boxes, box, key_list):
                opened_list.append(box)
                closed_list.remove(box)

    if len(closed_list) > 0:
        return False
    else:
        return True
