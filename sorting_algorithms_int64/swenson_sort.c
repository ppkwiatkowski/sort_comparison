#define SORT_NAME int64
#define SORT_TYPE int64_t
#define SORT_CMP(x, y)  ((x) < (y) ? -1 : ((x) == (y) ? 0 : 1))
#include "sort.h"

void tim_sort (int64_t* a, int64_t n){
	int64_tim_sort(a, n);
}

void shell_sort (int64_t* a, int64_t n){
	int64_shell_sort(a, n);
}

void binary_insertion_sort (int64_t* a, int64_t n){
	int64_binary_insertion_sort(a, n);
}

void heap_sort (int64_t* a, int64_t n){
	int64_heap_sort(a, n);
}

void quick_sort(int64_t* a, int64_t n){
	int64_quick_sort(a, n);
}

void merge_sort (int64_t* a, int64_t n){
	int64_merge_sort(a, n);
}

void selection_sort (int64_t* a, int64_t n){
	int64_selection_sort(a, n);
}

void grail_sort (int64_t* a, int64_t n){
	int64_grail_sort(a, n);
}

void sqrt_sort (int64_t* a, int64_t n){
	int64_sqrt_sort(a, n);
}