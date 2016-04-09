# In-place quicksort
def quicksort_cython_typed(list l):
    _quicksort(l, 0, len(l) - 1)


cdef void _quicksort(list l, int start, int stop):
    cdef int pivot, left, right
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
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1
        _quicksort(l, start, right)
        _quicksort(l, left, stop)
