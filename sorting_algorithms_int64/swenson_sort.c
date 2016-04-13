#define SORT_NAME sorter
#define SORT_TYPE int64_t
#define SORT_CMP(x, y) (x - y)
#include "sort.h"

void tim_sort (int64_t* a, int64_t n){
	sorter_tim_sort(a, n);
}

void shell_sort (int64_t* a, int64_t n){
	sorter_shell_sort(a, n);
}

void binary_insertion_sort (int64_t* a, int64_t n){
	sorter_binary_insertion_sort(a, n);
}

void heap_sort (int64_t* a, int64_t n){
	sorter_heap_sort(a, n);
}

void quick_sort(int64_t* a, int64_t n){
	sorter_quick_sort(a, n);
}

void merge_sort (int64_t* a, int64_t n){
	sorter_merge_sort(a, n);
}

void selection_sort (int64_t* a, int64_t n){
	sorter_selection_sort(a, n);
}