from libc.stdint cimport int64_t

cdef extern from "smoothsort.h":
    void smoothsort(int64_t *a, int n);