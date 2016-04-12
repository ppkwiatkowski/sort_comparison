#include <stdio.h>
#include <stdint.h>

void _quicksort (int64_t* l, int64_t start, int64_t stop) {
    int64_t pivot, left, right, tmp;
    if (stop - start > 0) {
        pivot = l[start];
        left = start;
        right = stop;
        while (left <= right) {
            while (l[left] < pivot)
                left += 1;
            while (l[right] > pivot)
                right -= 1;
            if (left <= right) {
                tmp = l[left];
                l[left] = l[right];
                l[right] = tmp;
                left += 1;
                right -= 1;
            }
        }
        _quicksort(l, start, right);
        _quicksort(l, left, stop);
    }
}

void quicksort (int64_t* a, int64_t n) {
    _quicksort(a, 0, n - 1);
}