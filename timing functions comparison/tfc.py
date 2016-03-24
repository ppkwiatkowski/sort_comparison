import sys
sys.path.insert(0, '..')
from sort_comp_lib import (time_algo_min, time_algo_mean,
                           time_algo_included_min, time_algo_included_mean,
                           gen_seq_complete_random)


# In-place quicksort
def quicksort(l):
    _quicksort(l, 0, len(l) - 1)


def _quicksort(l, start, stop):
    if stop - start > 0:
        pivot, left, right = l[start], start, stop
        while left <= right:
            while l[left] < pivot:
                left += 1
            while l[right] > pivot:
                right -= 1
            if left <= right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1
        _quicksort(l, start, right)
        _quicksort(l, left, stop)


print time_algo_min(fsort, gen_seq_complete_random(1000000))
