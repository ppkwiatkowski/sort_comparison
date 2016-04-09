#include <stdio.h>

void _quicksort (int* l, int start, int stop) {
    int pivot, left, right, tmp;
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

void quicksort (int* a, int n) {
    _quicksort(a, 0, n - 1);
}