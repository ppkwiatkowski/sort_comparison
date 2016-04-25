from libc.stdint cimport int64_t

cdef extern from "introsort.h":
    void IntroSort(int64_t *a, int n);