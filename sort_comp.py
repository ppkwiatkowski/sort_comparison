import argparse
import numpy as np
from sort_comp_lib import (is_sorted, gen_seq_np_almost_up, gen_seq_np_almost_down,
                           gen_seq_np_random_end, gen_seq_np_permutation,
                           time_algo_np_min, plot_bars)
from sorting_algorithms_int64.cy_swenson_sort import (tim_sort, shell_sort,
    binary_insertion_sort, heap_sort, quick_sort, merge_sort, selection_sort)

# Creating a simple command line arguments parser
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--correctness', action='store_true')
parser.add_argument('-b', '--basic', action='store_true')
parser.add_argument('-r', '--randomization', action='store_true')
parser.add_argument('-l', '--length', action='store_true')
args = parser.parse_args()


# Initialization
def fnames(flist):
    return [tmp.__name__ for tmp in flist]

N = 1000000
sorting_algorithms_funcions = [np.ndarray.sort, tim_sort, shell_sort,
                               heap_sort, quick_sort, merge_sort]
sorting_algorithms_names = fnames(sorting_algorithms_funcions)
seq_generators = [gen_seq_np_permutation, gen_seq_np_almost_up,
                  gen_seq_np_almost_down, gen_seq_np_random_end]
seq_gen_names = ['permutation', 'almost_up', 'almost_down', 'random_end']

# Checking if algorithms sort correctly
if args.correctness:  # Run with -c
    print "  Checking correctness.. "
    testseq = gen_seq_np_permutation(1000)
    for f in sorting_algorithms_funcions:
        testseqcopy = np.copy(testseq)
        f(testseqcopy)
        if is_sorted(testseqcopy):
            print "  " + f.__name__ + ".. \033[92m OK\033[00m"
        else:
            print "  " + f.__name__ \
                + ".. \033[91m Failed\033[00m"

# Bar plot comparison
if args.basic:  # Run with -b
    print "  Testing different types of sequences vs different types of " \
        "sorting algorithms.."
    print "  Generating test sequences.. "
    seqs = [seqgen(N) for seqgen in seq_generators]
    print "  Testing algorithms.."
    result = [[time_algo_np_min(f, seq)
               for f in sorting_algorithms_funcions] for seq in seqs]
    print "  Plotting results.."
    # pl.axis([0,4.5,0,0.4])
    plot_bars(result, sorting_algorithms_names,
              seq_gen_names, 'Test sequences length: ' + '{:,}'.format(N))
