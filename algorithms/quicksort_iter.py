import sys
import itertools
import numpy as np


def sort(list_, numIter=sys.maxint):
    """
    Iterative version of quick sort
    http://codexpi.com/quicksort-python-iterative-recursive-implementations/
    """

    left = 0
    right = len(list_) - 1
    temp_stack = []
    temp_stack.append((left, right))

    # Main loop to pop and push items until stack is empty
    iterCounter = itertools.count()
    while temp_stack:
        if iterCounter.next() > (numIter - 1):
            return -1
        pos = temp_stack.pop()
        right, left = pos[1], pos[0]
        # piv = partition_randomized(list_,left,right)
        piv = partition(list_, left, right)
        # If items in the left of the pivot push them to the stack
        if piv - 1 > left:
            temp_stack.append((left, piv - 1))
        # If items in the right of the pivot push them to the stack
        if piv + 1 < right:
            temp_stack.append((piv + 1, right))
    return list_


def partition(list_, left, right):
    """
    Partition method
    """
    # Pivot first element in the array
    piv = list_[left]
    i = left + 1
    j = right

    while 1:
        while i <= j and list_[i] <= piv:
            i += 1
        while j >= i and list_[j] >= piv:
            j -= 1
        if j <= i:
            break
        # Exchange items
        list_[i], list_[j] = list_[j], list_[i]
    # Exchange pivot to the right position
    list_[left], list_[j] = list_[j], list_[left]
    return j


def partition_randomized(list_, left, right, piv=-1):
    """
    Partition method
    but choses random pivot
    """

    # Pivot random element in the array
    if piv == -1:
        piv = list_[np.random.randint(left, right + 1)]
    i = left
    j = right

    while 1:
        while i <= j and list_[i] < piv:
            i += 1
        while j >= i and list_[j] > piv:
            j -= 1
        if j <= i:
            break
        # Exchange items
        list_[i], list_[j] = list_[j], list_[i]
    return j
