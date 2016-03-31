from cpython cimport array
import array

# In-place quicksort
def quicksort_cython_opt2(list l):
    cdef array.array a = array.array('i', l)
    cdef int[:] ca = a
    _quicksort(a, 0, len(a) - 1)


cdef void _quicksort(int[:] l, int start, int stop):
    cdef int pivot, left, right, tmp
    if stop - start > 0:
        pivot = l[start]
        left = start
        right = stop
        while left <= right:
            while l[left] < pivot:
                left += 1
            while l[right] > pivot:
                right -= 1
            if left <= right:
                tmp = l[left]
                l[left] = l[right]
                l[right] = tmp
                left += 1
                right -= 1
        _quicksort(l, start, right)
        _quicksort(l, left, stop)
