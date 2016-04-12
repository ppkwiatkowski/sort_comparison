from libc.stdint cimport int64_t
cimport quicksort

def quicksort_c(int64_t[::1] a):
    quicksort.quicksort(&a[0], a.size)