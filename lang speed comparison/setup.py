from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

ext = [
        Extension('quicksort_c', ['quicksort_c.pyx', 'quicksort.c']),
        Extension('quicksort_cython', ['quicksort_cython.pyx']),
        Extension('quicksort_cython_typed', ['quicksort_cython_typed.pyx']),
        Extension('quicksort_cython_numpy', ['quicksort_cython_numpy.pyx'])
      ]

setup(
    ext_modules=cythonize(ext)
)
