from libc.stdint cimport int64_t

cdef extern from "swenson_sort.h":
    void tim_sort (int64_t* a, int64_t n)
    void shell_sort (int64_t* a, int64_t n)
    void binary_insertion_sort (int64_t* a, int64_t n)
    void heap_sort (int64_t* a, int64_t n)
    void quick_sort(int64_t* a, int64_t n) 
    void merge_sort (int64_t* a, int64_t n)
    void selection_sort (int64_t* a, int64_t n)