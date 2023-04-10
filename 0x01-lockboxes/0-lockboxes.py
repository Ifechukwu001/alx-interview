#!/usr/bin/python3

"""Module containing the algorithm for lockboxes.

You have n number of locked boxes in front of you. 
Each box is numbered sequentially from 0 to n - 1 and 
each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """Can Unlock All: Checks if the boxes can all be opened.
    The function works you can test it on the main_0.py file.

    Args:
        boxes (list of list of int): Box list.

    Returns:
        bool: True if possible, False otherwise.
    """
    opened_list: list[int] = []
    closed_list: list[int] = []
    key_list: list[int] = [0]
    boxes_len = len(boxes)

    for box in range(boxes_len):
        if box in key_list:
            key_list.extend(boxes[box])
            opened_list.append(box)
        else:
            closed_list.append(box)

    if closed_list:
        for box in closed_list.copy():
            if box in key_list:
                key_list.extend(boxes[box])
                closed_list.remove(box)

    if len(closed_list) > 0:
        return False
    return True
