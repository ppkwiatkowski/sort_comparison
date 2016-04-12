from libc.stdint cimport int64_t

cdef extern from "quicksort.h":
    void quicksort (int64_t* a, int64_t n)