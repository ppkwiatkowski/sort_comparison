##Sort comparison##
####Overview####

`sort_comp.py` is a script written for testing modern sorting algorithms on different input sequence types. Sorting algorithms are written in `c` for efficiency, and wrapped with `cython` to become accesible from `python` level for convenience. 

Algorithms are tested on following sequence types [1]:
- permutation - completly random permutation
- almost_up - 90% of the items are in increasing order, but 10% of randomly-chosen items are random
- almost_down - like above, but the sorted items are in reverse order
- random_end - the array is already sorted, except for the last 256 items which are random

Sorted items are 64-bit integers.

####Results####

Following results come from tests performed on 2011 MacBook Pro with 2,3 GHz Intel Core i5:

######Bar plot comparison######
<img src="https://github.com/ppkwiatkowski/sort_comparison/blob/master/results/b_1kk.png">

######Increasing test sequence length######
<img src="https://github.com/ppkwiatkowski/sort_comparison/blob/master/results/l_permutation_1kk.png">
<img src="https://github.com/ppkwiatkowski/sort_comparison/blob/master/results/l_almost_up_1kk.png">
<img src="https://github.com/ppkwiatkowski/sort_comparison/blob/master/results/l_almost_down_1kk.png">
<img src="https://github.com/ppkwiatkowski/sort_comparison/blob/master/results/l_random_end_1kk.png">

######Increasing randomization######
<img src="https://github.com/ppkwiatkowski/sort_comparison/blob/master/results/r_1kk.png">

####How to run####
Scripts require `python 2.7` with installed `cython`, `numpy` and `matplotlib`.

Compilation of sorting algorithms in `c`:

    python sorting_algorithms_int64/setup.py build_ext --inplace

Plots a bar chart of algorithms speed on different input sequences: 

    python sort_comp.py -b [N=10000]
Linear plot of algorithm speed vs. sequence length for specific input sequence type:

    python sort_comp.py -l {permutation, almost_up, almost_down, random_end} [N=10000]
Plots algorithm speed vs. percantage of items that are not in order in the input sequence:

    python sort_comp.py -r [N=10000]
  
##Laguage speed comparison##
This is a simple test designed to compare the speed of python, cython and pure c code.
I am comparing the execution times of simple quicksort procedure, on sequences of different lengths.
Ale the files are in the `lang speed comparison\` folder. To run execute the following commands:
```
cd lang\ speed\ comparison/
python setup.py build_ext --inplace
python lang_speed_comp.py
```
Below are the results from the test performed on 2011 MacBook Pro with 2,3 GHz Intel Core i5:

<img width="400" src="https://raw.githubusercontent.com/ppkwiatkowski/sort_comparison/master/lang%20speed%20comparison/result_all.png">
<img width="400" src="https://raw.githubusercontent.com/ppkwiatkowski/sort_comparison/master/lang%20speed%20comparison/result_fast.png">

**quicksort_python** - pure python implementation<br/>
**list.sort** - default python method of sorting lists<br/>
**quicksort_cython** - python code compiled with cython<br/> 
**quicksort_cython_typed** - python code with typed variables compiled with cython<br/>
**quicksort_cython_numpy** - typed variables and run on `numpy.array`<br/>
**np.sort** - default numpy method of sorting arrays<br/>
**quicksort_c** - pure c code wrapped with cython<br/>

##References##
_________
- [1] http://warp.povusers.org/SortComparison/
- [2] https://github.com/swenson/sort
- [3] https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Smoothsort
