cimport introsort
from libc.stdint cimport int64_t

def intro_sort(int64_t[::1] a):
    introsort.IntroSort(&a[0], a.size)