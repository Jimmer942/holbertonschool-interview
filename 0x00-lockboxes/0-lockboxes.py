#!/usr/bin/python3
""" locked boxes """


def canUnlockAll(boxes):
    """
    INPUT a list of boxes with it's keys
    OUTPUT true if every box can be open flase otherwise
    """
    if len(boxes) == 1:
        return True
    key_chain = list()
    key_chain.append(0)
    for key in key_chain:
        if key < len(boxes):
            for open_box in boxes[key]:
                if open_box not in key_chain:
                    key_chain.append(open_box)
    if len(key_chain) == len(boxes):
        return True
    else:
        return False
