# Insertion sort with binary search
# Code from http://rosettacode.org/
import bisect


def sort(seq):
    for i in range(1, len(seq)):
        bisect.insort(seq, seq.pop(i), 0, i)
    return seq
