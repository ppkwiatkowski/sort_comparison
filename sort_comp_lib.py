import numpy as np
import matplotlib.pyplot as plt
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


def time_algo(sort_fun, input_seq_generator, N, num=10):
    print "        Testing " + sort_fun.__name__ + " on " \
          + input_seq_generator.__name__
    results = []
    for i in xrange(num):
        input_seq = input_seq_generator(N)
        results.append(time_algo_np_min(sort_fun, input_seq))
    return (sum(results) / len(results), min(results), max(results))


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

def gen_seq_np_almost_up(n, percentRand=10):
    result = np.arange(n)
    numRand = int((percentRand / 100.0) * n)
    choices = iter(np.random.choice(range(n), numRand, replace=False))
    for count in xrange(int(numRand / 2)):
        i1 = choices.next()
        i2 = choices.next()
        result[i1], result[i2] = result[i2], result[i1]
    return result


def gen_seq_np_almost_down(n, percentRand=10):
    result = gen_seq_np_almost_up(n, percentRand)
    result = result[::-1].copy()
    return result


def gen_seq_np_permutation(n):
    return np.random.permutation(n)


def gen_seq_np_random_end(n, nRandom=256):
    result = np.array(range(n - nRandom)) * 2
    randInts = np.random.choice(result + 1, nRandom, replace=False)
    return np.concatenate((result, randInts))


def gen_seq_np_completely_random(n):
    type_info = np.iinfo(np.int64)
    return np.random.random_integers(type_info.min, type_info.max, n)


def gen_seq_np_duplicates(n, uniques=10):
    type_info = np.iinfo(np.int64)
    unique_values = np.random.random_integers(type_info.min, type_info.max,
                                              uniques)
    return np.random.choice(unique_values, n)


# Plotting functions

def plot_bars(result, algo_names, seq_names, title='', spacer=2,
              bar_width=0.25):
    n = len(result[0])
    group_len = float(len(seq_names))
    spacer_val = (group_len + spacer) * bar_width
    # ind = the x locations for the groups
    ind = np.arange(n) * spacer_val + (spacer_val - group_len / 2 * bar_width)
    coloriter = iter([
        '#DECF3F',  # yellow
        '#5DA5DA',  # blue
        '#FAA43A',  # orange
        '#60BD68',  # green
        '#F15854',  # red
        '#B276B2',  # purple
        '#F17CB0',  # pink
        '#B2912F',  # brown
        '#4D4D4D',  # gray
    ])
    labeliter = iter(seq_names)

    fig, ax = plt.subplots()
    for i, r in enumerate(result):
        ax.bar(ind + bar_width * i, r, bar_width, color=coloriter.next(),
               label=labeliter.next(), zorder=3)

    plt.xlim([min(ind) - spacer * bar_width,
              max(ind) + (group_len + spacer) * bar_width])
    plt.title(title)
    plt.xticks(ind + group_len / 2 * bar_width, algo_names)
    plt.xticks(rotation=45)
    plt.ylabel('Time (s)')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax.yaxis.grid(True, zorder=0)
    plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.5, frameon=False)
    fig.subplots_adjust(right=0.76, bottom=0.15)
    plt.show()


def plot_bars_e(result, algo_names, seq_names, title='', spacer=2,
                bar_width=0.25):
    n = len(result[0])
    group_len = float(len(seq_names))
    spacer_val = (group_len + spacer) * bar_width
    # ind = the x locations for the groups
    ind = np.arange(n) * spacer_val + (spacer_val - group_len / 2 * bar_width)
    coloriter = iter([
        '#DECF3F',  # yellow
        '#5DA5DA',  # blue
        '#FAA43A',  # orange
        '#60BD68',  # green
        '#F15854',  # red
        '#B276B2',  # purple
        '#F17CB0',  # pink
        '#B2912F',  # brown
        '#4D4D4D',  # gray
    ])
    labeliter = iter(seq_names)

    fig, ax = plt.subplots()
    for i, r in enumerate(result):
        barh = [x[0] for x in r]
        min_e = [x[0] - x[1] for x in r]
        max_e = [x[2] - x[0] for x in r]
        ax.bar(ind + bar_width * i, barh, bar_width, color=coloriter.next(),
               label=labeliter.next(), zorder=3)
        ax.errorbar(ind + bar_width * i + bar_width / 2, barh, fmt='none',
                    yerr=[min_e, max_e], ecolor='#4D4D4D', zorder=4)

    plt.xlim([min(ind) - spacer * bar_width,
              max(ind) + (group_len + spacer) * bar_width])
    plt.title(title)
    plt.xticks(ind + group_len / 2 * bar_width, algo_names)
    plt.xticks(rotation=45)
    plt.ylabel('Time (s)')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax.yaxis.grid(True, zorder=0)
    plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.5, frameon=False)
    fig.subplots_adjust(right=0.76, bottom=0.15)
    plt.show()


def plot_linear(result, algo_names, xs=[], xlabel="", ylabel="", title="",
                scix=False, sciy=False):
    if xs == []:
        xs = range(len(result))
    labeliter = iter(['r-', 'g-', 'b-', 'c-', 'm-', 'y-', 'k-',
                      'r--', 'g--', 'b--', 'c--', 'm--', 'y--', 'k--',
                      'r:', 'g:', 'b:', 'c:', 'm:', 'y:', 'k:'])
    fig, ax = plt.subplots()
    for res in result:
        plt.plot(xs, res, labeliter.next(), zorder=3)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if scix:
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    if sciy:
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.grid(True, zorder=0)
    plt.legend(algo_names, bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.,
               frameon=False)
    fig.subplots_adjust(right=0.76, bottom=0.12)
    plt.axis('tight')
    plt.show()


# Other useful functions

def is_sorted(a):
        return all(a[i] <= a[i + 1] for i in xrange(len(a) - 1))
