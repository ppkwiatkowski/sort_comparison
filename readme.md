###Sort comparison###
The main functionality is still under development...
###Laguage speed comparison###
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
