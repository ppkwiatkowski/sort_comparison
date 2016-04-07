import sys
import matplotlib.pyplot as plt
from quicksort_python import quicksort_python
from quicksort_cython import quicksort_cython
from quicksort_cython_opt import quicksort_cython_opt
from quicksort_cython_opt3 import quicksort_cython_opt3
import numpy as np

sys.path.insert(0, '..')
from sort_comp_lib import (time_algo_min, gen_seq_complete_random,
                           time_algo_np_min, gen_seq_np_permutation)


# seq_lengths = [10]
seq_lengths = [10, 50, 100, 500, 1000, 5000]
# seq_lengths = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000,
#                1000000, 5000000, 10000000]


def wrapper(f, l):
    print (f.__name__ + ' %d') % l
    return time_algo_min(f, gen_seq_complete_random(l), 100)


def wrapper_np(f, l):
    print (f.__name__ + ' %d') % l
    foo = gen_seq_np_permutation(l)
    return time_algo_np_min(f, foo, 100)

d_quicksort_python = [wrapper(quicksort_python, l) for l in seq_lengths]
# d_quicksort_python_np = [wrapper_np(quicksort_python, l)
#                          for l in seq_lengths]
d_list_sort = [wrapper(list.sort, l) for l in seq_lengths]
d_quicksort_cython = [wrapper(quicksort_cython, l) for l in seq_lengths]
d_quicksort_cython_opt = [wrapper(quicksort_cython_opt, l)
                          for l in seq_lengths]
d_quicksort_cython_opt3 = [wrapper_np(quicksort_cython_opt3, l)
                           for l in seq_lengths]
d_np_sort = [wrapper_np(np.sort, l) for l in seq_lengths]

plt.plot(seq_lengths, d_quicksort_python,
         '--', marker='x', label='quicksort_python')
plt.plot(seq_lengths, d_list_sort,
         '--', marker='x', label='list.sort')
# plt.plot(seq_lengths, d_quicksort_python_np,
#         '--', marker='x', label='quicksort_python_numpy')
plt.plot(seq_lengths, d_quicksort_cython,
         '--', marker='x', label='quicksort_cython')
plt.plot(seq_lengths, d_quicksort_cython_opt,
         '--', marker='x', label='quicksort_cython_opt')
plt.plot(seq_lengths, d_quicksort_cython_opt3,
         '--', marker='x', label='quicksort_cython_opt3')
plt.plot(seq_lengths, d_np_sort, '--', marker='x', label='np.sort')

plt.grid(True)
plt.xlabel('sequence length')
plt.ylabel('time (s)')
plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0., frameon=False)
plt.show()
