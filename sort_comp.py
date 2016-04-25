import argparse
import numpy as np
import pylab as pl
import sys
from sort_comp_lib import (is_sorted, gen_seq_np_almost_up,
                           gen_seq_np_almost_down, gen_seq_np_random_end,
                           gen_seq_np_permutation, time_algo_np_min, plot_bars,
                           plot_linear)
from sorting_algorithms_int64.cy_swenson_sort import (tim_sort, shell_sort,
                                                      binary_insertion_sort,
                                                      heap_sort, quick_sort,
                                                      merge_sort, grail_sort,
                                                      selection_sort,
                                                      sqrt_sort)
from sorting_algorithms_int64.cy_introsort import intro_sort
# from sorting_algorithms_int64.cy_cubesort import cube_sort
from sorting_algorithms_int64.cy_smoothsort import smooth_sort

# Creating a simple command line arguments parser
parser = argparse.ArgumentParser()
parser.add_argument('N', type=int, default=10000, nargs='?',
                    help='test sequences max length, default = 10000')
parser.add_argument('-c', '--correctness', action='store_true',
                    help='check if algos correctly sort N elem permutation')
parser.add_argument('-b', '--bar', action='store_true',
                    help='bar plot of different algos on different seqs')
parser.add_argument('-r', '--randomization', action='store_true',
                    help='behavior on almost_up seqs with different random %%')
parser.add_argument('-l', '--length', choices=['almost_up', 'almost_down',
                    'permutation', 'random_end'],
                    help='bahavior on specific seq with increasing length')
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()


# Initialization
def fnames(flist):
    return [tmp.__name__ for tmp in flist]

N = args.N
sorting_algorithms_funcions = [np.ndarray.sort, tim_sort, shell_sort,
                               heap_sort, quick_sort, merge_sort, intro_sort,
                               smooth_sort, grail_sort, sqrt_sort]
sorting_algorithms_names = fnames(sorting_algorithms_funcions)
seq_generators = [gen_seq_np_permutation, gen_seq_np_almost_up,
                  gen_seq_np_almost_down, gen_seq_np_random_end]
seq_gen_names = ['permutation', 'almost_up', 'almost_down', 'random_end']

# Checking if algorithms sort correctly
if args.correctness:  # Run with -c
    print "  Checking correctness.. "
    testseq = gen_seq_np_permutation(N)
    for f in sorting_algorithms_funcions:
        testseqcopy = np.copy(testseq)
        f(testseqcopy)
        if is_sorted(testseqcopy):
            print "  " + f.__name__ + ".. \033[92m OK\033[00m"
        else:
            print "  " + f.__name__ \
                + ".. \033[91m Failed\033[00m"

# Bar plot comparison
if args.bar:  # Run with -b
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

# Studying the effect of increasing randomization
if args.randomization:  # Run with -r
    print "  Testing effect of different levels of randomization.."
    randpers = pl.linspace(1, 60, 25)
    print "  Generating test sequences.."
    seqs = [gen_seq_np_almost_up(N, tmp) for tmp in randpers]
    print "  Testing algorithms.."
    result = [[time_algo_np_min(f, seq)
              for seq in seqs] for f in sorting_algorithms_funcions]
    print "  Plotting results.."
    plot_linear(result, sorting_algorithms_names, xs=randpers,
                xlabel="Percent randomization", ylabel="Time (s)")

# Studying the effect of increasing sequence length
if args.length:  # Run with -l <seq_name>
    print "  Testing " + args.length + " sequences of different lengths..."
    testlens = pl.linspace(1000, N, 10)
    print "  Generating test sequences.."
    choices = {'almost_up': gen_seq_np_almost_up,
               'almost_down': gen_seq_np_almost_down,
               'permutation': gen_seq_np_permutation,
               'random_end': gen_seq_np_random_end}
    seqs = [choices[args.length](int(tmp)) for tmp in testlens]
    print "  Testing algorithms.."
    result = [[time_algo_np_min(f, seq)
              for seq in seqs] for f in sorting_algorithms_funcions]
    print "  Plotting results.."
    plot_linear(result, sorting_algorithms_names, xs=testlens,
                xlabel="Sequence Length", ylabel="Time (s)", title=args.length)
