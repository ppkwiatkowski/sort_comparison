cimport smoothsort
from libc.stdint cimport int64_t

def smooth_sort(int64_t[::1] a):
    smoothsort.smoothsort(&a[0], a.size)