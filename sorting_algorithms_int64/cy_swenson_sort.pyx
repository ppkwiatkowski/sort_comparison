cimport swenson_sort
from libc.stdint cimport int64_t

def tim_sort(int64_t[::1] a):
    swenson_sort.tim_sort(&a[0], a.size)

def shell_sort(int64_t[::1] a):
    swenson_sort.shell_sort(&a[0], a.size)

def binary_insertion_sort(int64_t[::1] a):
    swenson_sort.binary_insertion_sort(&a[0], a.size)

def heap_sort(int64_t[::1] a):
    swenson_sort.heap_sort(&a[0], a.size)

def quick_sort(int64_t[::1] a):
    swenson_sort.quick_sort(&a[0], a.size)

def merge_sort(int64_t[::1] a):
    swenson_sort.merge_sort(&a[0], a.size)

def selection_sort(int64_t[::1] a):
    swenson_sort.selection_sort(&a[0], a.size)

def grail_sort(int64_t[::1] a):
    swenson_sort.grail_sort(&a[0], a.size)

def sqrt_sort(int64_t[::1] a):
    swenson_sort.sqrt_sort(&a[0], a.size)