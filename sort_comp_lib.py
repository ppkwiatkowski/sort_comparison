import numpy as np
import pylab as pl
import timeit


# Timing fuctions working on lists

def time_algo_min(sort_fun, input_seq, num=10):
    '''
    Time how long it takes to sort sequence 'input_seq' using
    function 'sort_fun'. Take min of 'num' times.
    '''
    def wrapped():
        sort_fun(foo)

    def reset_seq():
        foo[:] = input_seq[:]

    foo = []
    return min(timeit.timeit(wrapped, setup=reset_seq,
                             number=1) for _ in range(num))


def time_algo_mean(sort_fun, input_seq, num=10):
    '''
    Time how long it takes to sort sequence 'input_seq' using
    function 'sort_fun'.
    Repeat 'num' times and return tuple (min, mean).
    '''
    def wrapped():
        sort_fun(foo)

    def reset_seq():
        foo[:] = input_seq[:]

    foo = []
    result = list(timeit.timeit(wrapped, setup=reset_seq,
                                number=1) for _ in range(num))
    return sum(result) / len(result)


def time_algo_included_min(sort_fun, input_seq, num=10):
    '''
    Time how long it takes to sort sequence 'input_seq' using
    function 'sort_fun'.
    Copying of 'input_seq' timing included.
    Return min of 'num' runs.
    '''
    def wrapped():
        sort_fun(input_seq[:])

    return min(timeit.repeat(wrapped, repeat=num, number=1))


def time_algo_included_mean(sort_fun, input_seq, num=10):
    '''
    Time how long it takes to sort sequence 'input_seq' using
    function 'sort_fun'.
    Copying of 'input_seq' timing included.
    Return mean of 'num' runs.
    '''
    def wrapped():
        sort_fun(input_seq[:])

    return timeit.timeit(wrapped, number=num) / num


# Timing functions working on numpy arrays

def time_algo_np_min(sort_fun, input_seq, num=10):
    '''
    Time how long it takes to sort sequence 'input_seq' using
    function 'sort_fun'. Take min of 'num' times.
    'input_seq' is a numpy array.
    '''
    foo = np.array([], dtype=np.intc)

    def wrapped():
        global foo
        sort_fun(foo)

    def reset_seq():
        global foo
        foo = input_seq.copy()

    return min(timeit.timeit(wrapped, setup=reset_seq,
                             number=1) for _ in range(num))


# Test sequences generators returning lists
# Based on: http://warp.povusers.org/SortComparison/

def gen_seq_almost_up(n, percentRand=10):
    result = range(n)
    numRand = int((percentRand / 100.0) * n)
    choices = iter(np.random.choice(range(n), numRand, replace=False))
    for count in range(int(numRand / 2)):
        i1 = choices.next()
        i2 = choices.next()
        tmp = result[i1]
        result[i1] = result[i2]
        result[i2] = tmp
    return result


def gen_seq_almost_down(n, percentRand=10):
    result = gen_seq_almost_up(n, percentRand)
    result.reverse()
    return result


def gen_seq_permutation(n):
    return np.random.permutation(n).tolist()


def gen_seq_random_end(n, nRandom=256):
    result = np.array(range(n - nRandom)) * 2
    randInts = np.random.choice(result + 1, nRandom, replace=False)
    return list(np.concatenate((result, randInts)))


# Test sequences generators returning numpy arrays

def gen_seq_np_permutation(n):
    return np.random.permutation(n).astype(np.int32)

# Plotting functions

def PlotCompBar(result, algoNames, seqNames, plotTitle='', spacer=1.5,
                barWidth=0.25, loc=2):
    n_groups = len(result[0])
    index = np.arange(n_groups)*spacer+0.2
    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    pl.hold('on')

    bariter = iter(xrange(10))
    labeliter = iter(seqNames)
    coloriter = iter(['r', 'g', 'b', 'm', 'y'])

    for res in result:
        rects1 = pl.bar(index + barWidth * bariter.next(), res,
                        barWidth, alpha=opacity, color=coloriter.next(),
                        label=labeliter.next())

    pl.xticks(rotation=45)
    pl.xlabel('Algorithm')
    pl.ylabel('Time(s)')
    pl.title(plotTitle)
    pl.xticks(index + barWidth, algoNames)
    pl.legend(loc=loc)
    pl.plot(0, 0, 'w.')
    pl.tight_layout()
    pl.show()


def PlotAlgoTimes(result, algoNames, xValues=[], xLabel="", yLabel="",
                  plotTitle="", newFig=True, loc=2):

    if newFig:
        pl.figure()

    pl.hold('on')
    if xValues == []:
        xValues = range(len(result))
    labeliter = iter(['r-', 'g-', 'b-', 'c-', 'm-', 'y-', 'k-',
                      'r--', 'g--', 'b--', 'c--', 'm--', 'y--', 'k--',
                      'r:', 'g:', 'b:', 'c:', 'm:', 'y:', 'k:'])
    for res in result:
        pl.plot(xValues, res, labeliter.next())
    pl.legend(algoNames, loc=loc)
    pl.axis('tight')
    pl.title(plotTitle)
    pl.xlabel(xLabel)
    pl.ylabel(yLabel)
    pl.show()


# Other usefull functions

def is_sorted(a):
        return all(a[i] <= a[i+1] for i in xrange(len(a)-1))
