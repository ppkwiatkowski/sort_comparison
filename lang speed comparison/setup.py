from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='quicksort cython',
    ext_modules=cythonize("*.pyx"),
)
