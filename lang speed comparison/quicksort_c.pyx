cimport quicksort

def quicksort_c(int[::1] a):
    quicksort.quicksort(&a[0], a.size)