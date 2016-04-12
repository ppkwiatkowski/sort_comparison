import sys
import matplotlib.pyplot as plt
from quicksort_python import quicksort_python
from quicksort_cython import quicksort_cython
from quicksort_cython_typed import quicksort_cython_typed
from quicksort_cython_numpy import quicksort_cython_numpy
from quicksort_c import quicksort_c
import numpy as np

sys.path.insert(0, '..')
from sort_comp_lib import (time_algo_min, gen_seq_permutation,
                           time_algo_np_min, gen_seq_np_permutation,
                           is_sorted)


seq_lengths = [10, 50, 100, 500, 1000, 5000]
# seq_lengths = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000
#               1000000, 5000000, 10000000]

# check correctness of sorting functions
sorting_functions_list = [quicksort_python, quicksort_cython,
                          quicksort_cython_typed]
sorting_functions_np = [quicksort_cython_numpy, quicksort_c]

for f in sorting_functions_list:
    foo = gen_seq_permutation(1000)
    f(foo)
    if (is_sorted(foo)):
        print (f.__name__ + '.. OK')
    else:
        print (f.__name__ + '.. FAILED')

for f in sorting_functions_np:
    foo = gen_seq_np_permutation(1000)
    f(foo)
    if (is_sorted(foo)):
        print (f.__name__ + '.. OK')
    else:
        print (f.__name__ + '.. FAILED')


def wrapper(f, l):
    print (f.__name__ + ' %d') % l
    return time_algo_min(f, gen_seq_permutation(l), 100)


def wrapper_np(f, l):
    print (f.__name__ + ' %d') % l
    return time_algo_np_min(f, gen_seq_np_permutation(l), 100)

d_quicksort_python = [wrapper(quicksort_python, l) for l in seq_lengths]
# d_quicksort_python_np = [wrapper_np(quicksort_python, l)
#                          for l in seq_lengths]
d_list_sort = [wrapper(list.sort, l) for l in seq_lengths]
d_quicksort_cython = [wrapper(quicksort_cython, l) for l in seq_lengths]
d_quicksort_cython_typed = [wrapper(quicksort_cython_typed, l)
                            for l in seq_lengths]
d_quicksort_cython_numpy = [wrapper_np(quicksort_cython_numpy, l)
                            for l in seq_lengths]
d_np_sort = [wrapper_np(np.sort, l) for l in seq_lengths]
d_quicksort_c = [wrapper_np(quicksort_c, l) for l in seq_lengths]

plt.plot(seq_lengths, d_quicksort_python,
         '--', marker='x', label='quicksort_python')
plt.plot(seq_lengths, d_list_sort,
         '--', marker='x', label='list.sort')
# plt.plot(seq_lengths, d_quicksort_python_np,
#         '--', marker='x', label='quicksort_python_numpy')
plt.plot(seq_lengths, d_quicksort_cython,
         '--', marker='x', label='quicksort_cython')
plt.plot(seq_lengths, d_quicksort_cython_typed,
         '--', marker='x', label='quicksort_cython_typed')
plt.plot(seq_lengths, d_quicksort_cython_numpy,
         '--', marker='x', label='quicksort_cython_numpy')
plt.plot(seq_lengths, d_np_sort, '--', marker='x', label='np.sort')
plt.plot(seq_lengths, d_quicksort_c, '--', marker='x', label='quicksort_c')

plt.grid(True)
plt.xlabel('sequence length')
plt.ylabel('time (s)')
plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0., frameon=False)
plt.show()
