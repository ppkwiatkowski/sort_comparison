import sys
import os
import re
#import pylab as pl
import numpy as np
import argparse
import copy
from sortzilla import (TimeAlgo, seqGenerators, PlotCompBar, PlotAlgoTimes,
                       AlmostUp, RandomEnd, CompleteRandom)
from sorting_algorithms_int64.timsort_c import timsort_c

# Creating a simple command line arguments parser
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--correctness', action='store_true')
parser.add_argument('-b', '--basic', action='store_true')
parser.add_argument('-r', '--randomization', action='store_true')
parser.add_argument('-l', '--length', action='store_true')
args = parser.parse_args()

# Initializations and creating utility functions
testLen = 10000


def fnames(flist):
    return [tmp.func_name for tmp in flist]

# Importing sort functions from algorithms directory
path = os.path.abspath(os.path.dirname(sys.argv[0])) + '/algorithms/'
sys.path.append(path)
files = os.listdir(path)
regex = re.compile("\.py$", re.IGNORECASE)
files = filter(regex.search, files)
sortingAlgorithmsNames = map((lambda f: os.path.splitext(f)[0]), files)
# Removing slow algorithms
sortingAlgorithmsNames.remove('bubble_sort')
sortingAlgorithmsNames.remove('selection_sort')
sortingAlgorithmsNames.remove('quicksort_iter')
sortingAlgorithmsNames.remove('cycle_sort')
sortingAlgorithmsNames.remove('strand_sort')
sortingAlgorithmsNames.remove('setup')
sortingAlgorithmsNames.append('quicksort_rec_c')
sortingAlgorithmsNames.append('Timsort_c')
sortingAlgorithmsNames.append('heapsort_c')
sortingAlgorithmsNames.append('insertion_sort_bin_c')
sortingAlgorithmsNames.append('comb_sort_c')
sortingAlgorithmsNames.append('merge_sort_c')
sortingAlgorithmsNames.append('shell_sort_c')
sortingAlgorithmsNames.append('patience_sort_c')
list.sort(sortingAlgorithmsNames)
# Timsort @ relative path - check algorithms/Timsort.py and fix path to run
# sortingAlgorithmsNames.remove('Timsort')

print "  Loaded algorithms: {}".format(', '.join(sortingAlgorithmsNames))
functions = map(__import__, sortingAlgorithmsNames)


class timsort:
    @staticmethod
    def sort(l):
        foo = np.array(l)
        timsort_c(foo)


functions.append(timsort)
sortingAlgorithmsNames.append('timsort_c')

# Checking if algorithms sort correctly
if args.correctness:  # Run with -c
    print "  Checking correctness.. "

    def isSorted(list):
        return all(list[i] <= list[i+1] for i in xrange(len(list)-1))

    testseq = CompleteRandom(testLen)
    for x in xrange(0, len(sortingAlgorithmsNames)):
        testseqcopy = copy.copy(testseq)
        if isSorted(functions[x].sort(testseqcopy)):
            print "  " + sortingAlgorithmsNames[x] + ".. \033[92m OK\033[00m"
        else:
            print "  " + sortingAlgorithmsNames[x] \
                + ".. \033[91m Failed\033[00m"

# Creating the bar charts in the povusers study
if args.basic:  # Run with -b
    print "  Testing different types of sequences vs different types of " \
        "sorting algorithms.."
    print "  Generating test sequences.. "
    seqs = [seqgen(testLen) for seqgen in seqGenerators]
    print "  Testing algorithms.."
    result = [[TimeAlgo((lambda x:f.sort(x)), seq)
               for f in functions] for seq in seqs]
    print "  Plotting results.."
    # pl.axis([0,4.5,0,0.4])
    PlotCompBar(result, sortingAlgorithmsNames,
                fnames(seqGenerators), 'Sequence Length: ' + str(testLen))

# Studying the effect of increasing randomization
if args.randomization:  # Run with -r
    print "  Testing effect of different levels of randomization.."
    randpers = pl.linspace(5, 60, 20)
    print "  Generating test sequences.."
    seqs = [AlmostUp(testLen, tmp) for tmp in randpers]
    print "  Testing algorithms.."
    result = np.array([[TimeAlgo((lambda x:f.sort(x)), seq)
                        for seq in seqs] for f in functions])
    print "  Plotting results.."
    PlotAlgoTimes(result, sortingAlgorithmsNames, xValues=randpers,
                  xLabel="Percent randomization", yLabel="Time (s)")

# Studying the effect of the sequence length and RandomEnd sequence
if args.length:  # Run with -l
    print "  Testing 'RandomEnd' sequences of different lengths..."
    testlens = pl.linspace(1000, 50000, 8)
    print "  Generating test sequences.."
    seqs = [RandomEnd(int(tmp)) for tmp in testlens]
    print "  Testing algorithms.."
    result = [[TimeAlgo((lambda x:f.sort(x)), seq)
               for seq in seqs] for f in functions]
    print "  Plotting results.."
    PlotAlgoTimes(result, sortingAlgorithmsNames, xValues=testlens,
                  xLabel="Sequence Length", yLabel="Time (s)")
