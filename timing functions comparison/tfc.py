import sys
import matplotlib.pyplot as plt
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


seq_lengths = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 1000000]


def wrapper(f, l):
    print (f.__name__ + ' %d') % l
    return f(quicksort, gen_seq_complete_random(l))

d_time_algo_min = [wrapper(time_algo_min, l) for l in seq_lengths]
d_time_algo_mean = [wrapper(time_algo_mean, l) for l in seq_lengths]
d_time_algo_included_min = [wrapper(time_algo_included_min, l)
                            for l in seq_lengths]
d_time_algo_included_mean = [wrapper(time_algo_included_mean, l)
                             for l in seq_lengths]

plt.plot(seq_lengths, d_time_algo_min, '--', label='min')
plt.plot(seq_lengths, d_time_algo_mean, '--', label='mean')
plt.plot(seq_lengths, d_time_algo_included_min, '--', label='included_min')
plt.plot(seq_lengths, d_time_algo_included_mean, '--', label='included_mean')
plt.xlabel('sequence length')
plt.ylabel('time (s)')
plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0., frameon=False)
plt.show()
