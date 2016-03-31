import sys
import matplotlib.pyplot as plt
from quicksort_python import quicksort_python
from quicksort_cython import quicksort_cython
from quicksort_cython_opt import quicksort_cython_opt
from quicksort_cython_opt2 import quicksort_cython_opt2

sys.path.insert(0, '..')
from sort_comp_lib import time_algo_min, gen_seq_complete_random


seq_lengths = [10, 50, 100, 500, 1000, 5000, 10000]


def wrapper(f, l):
    print (f.__name__ + ' %d') % l
    return time_algo_min(f, gen_seq_complete_random(l), 100)


d_quicksort_python = [wrapper(quicksort_python, l) for l in seq_lengths]
d_quicksort_cython = [wrapper(quicksort_cython, l) for l in seq_lengths]
d_quicksort_cython_opt = [wrapper(quicksort_cython_opt, l)
                          for l in seq_lengths]
d_quicksort_cython_opt2 = [wrapper(quicksort_cython_opt2, l)
                          for l in seq_lengths]

plt.plot(seq_lengths, d_quicksort_python,
         '--', marker='x', label='quicksort_python')
plt.plot(seq_lengths, d_quicksort_cython,
         '--', marker='x', label='quicksort_cython')
plt.plot(seq_lengths, d_quicksort_cython_opt,
         '--', marker='x', label='quicksort_cython_opt')
plt.plot(seq_lengths, d_quicksort_cython_opt2,
         '--', marker='x', label='quicksort_cython_opt2')

plt.grid(True)
plt.xlabel('sequence length')
plt.ylabel('time (s)')
plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0., frameon=False)
plt.show()
