#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from
0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
     a method that determines if all the boxes can be opened.


    :param boxes:
    :return: True or False
    """
    opened = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        opened.add(current_box)
        keys = boxes[current_box]

        for key in keys:
            if key >= 0 and key < len(boxes) and key not in opened:
                stack.append(key)

    return len(opened) == len(boxes)
