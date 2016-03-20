# Code from http://rosettacode.org/


def sort(lst):
    for i, e in enumerate(lst):
        mn = min(range(i, len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], e
    return lst
