/*
 * Introsort for int64_t.
 * by Lev Panov, 2010
 * and possibly others
 */

#include <math.h>
#include <stdint.h>

#define swap(a, b) { \
		register int64_t tmp = *(a); \
		*(a) = *(b); \
		*(b) = tmp; \
}

/* default value: */
#define size_threshold 16
//#define size_threshold 64

inline static int floor_lg(int a);
static int partition(int64_t *a, int lo, int hi, int64_t x);
static int64_t medianof3(int64_t *a, int lo, int mid, int hi);
static void insertionsort(int64_t *a, int lo, int hi);
static void downheap(int64_t *a, int i, int n, int lo);
static void heapsort(int64_t *a, int lo, int hi );
static void introsort_loop(int64_t *a, int lo, int hi, int depth_limit);

void IntroSort(int64_t *a, int n)
{
	introsort_loop(a, 0, n, 2 * floor_lg(n));
	insertionsort(a, 0, n);
}

static void introsort_loop(int64_t *a, int lo, int hi, int depth_limit)
{
	int p;

	while (hi - lo > size_threshold)
	{
		if (depth_limit == 0)
		{
			heapsort(a, lo, hi);
			return;
		}
		
		depth_limit--;
	    p = partition(a, lo, hi, 
			medianof3(a, lo, lo + ((hi - lo) / 2) + 1, hi - 1));
	    introsort_loop(a, p, hi, depth_limit);
	    hi = p;
	}
}

static int partition(int64_t *a, int lo, int hi, int64_t x)
{
	int i = lo, j = hi;
	
	while (1)
	{
		while (a[i] < x)
			i++;
		j--;
		while (x < a[j]) 
			j--;
		if (i >= j)
			return i;
		swap(&a[i], &a[j]);
		i++;
    }
}

static int64_t medianof3( int64_t *a, int lo, int mid, int hi )
{
	if (a[mid] < a[lo])
	{
		if (a[hi] < a[mid])
			return a[mid];
		else
		{
			if (a[hi] < a[lo])
				return a[hi];
			else
				return a[lo];
		}
	}
	else
	{
		if (a[hi] < a[mid])
		{
			if (a[hi] < a[lo])
				return a[lo];
			else
				return a[hi];
		}
		else
			return a[mid];
	}
}

static void heapsort(int64_t *a, int lo, int hi)
{
	int n = hi - lo;
	int i;
	
	for (i = n / 2; i >= 1; i--)
	{
		downheap(a, i, n, lo);
	}
	
	for (i = n; i > 1; i--)
	{
		swap(&a[lo], &a[lo + i - 1]);
		downheap(a, 1, i - 1, lo);
	}
}

static void downheap(int64_t *a, int i, int n, int lo)
{
	int64_t d = a[lo + i - 1];
	int child;
	int n2 = n / 2;
	
	while (i <= n2)
	{
		child = 2 * i;
		if (child < n && a[lo + child - 1] < a[lo + child])
			child++;
		if (d >= a[lo + child - 1])
			break;
		a[lo + i - 1] = a[lo + child - 1];
		i = child;
	}
	
	a[lo + i - 1] = d;
}

static void insertionsort(int64_t *a, int lo, int hi)
{
	int i, j;
	int64_t t;
	
	for (i = lo; i < hi; i++)
	{
		j = i;
	    t = a[i];
	    while (j != lo && t < a[j - 1])
		{
			a[j] = a[j - 1];
			j--;
		}
		a[j] = t;
	}
}

inline static int floor_lg(int a)
{
	return (int)floor(log(a) / log(2));
}