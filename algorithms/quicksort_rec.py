from random import *


def sort(a):
    if len(a) <= 1:
        return a
    else:
        q = choice(a)
        return sort([elem for elem in a if elem < q]) + [q] * a.count(q) \
            + sort([elem for elem in a if elem > q])
