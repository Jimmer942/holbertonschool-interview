#!/usr/bin/python3
""" locked boxes """


def canUnlockAll(boxes):
    """
    INPUT a list of boxes with it's keys
    OUTPUT true if every box can be open flase otherwise
    """
    key_chain = list()
    room = list()
    key_chain.append(0)

    for key in key_chain:
        for k in boxes[key]:
            if k not in key_chain:
                key_chain.append(k)
    if len(key_chain) == len(boxes):
        return True
    else:
        return False
