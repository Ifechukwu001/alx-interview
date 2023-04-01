#!/usr/bin/python3
"""Module containing the algorithm for lockboxes.
The Algorithm has a time complexity of O(n).
"""


def canUnlockAll(boxes: list[list[int]]) -> bool:
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
