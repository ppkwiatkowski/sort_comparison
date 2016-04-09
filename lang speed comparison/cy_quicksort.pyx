cimport quicksort

def quicksort_c(int[::1] a):
    quicksort.quick_sort(&a[0], a.size)