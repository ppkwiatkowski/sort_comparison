from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

ext = [
        Extension('cy_swenson_sort', ['cy_swenson_sort.pyx', 'swenson_sort.c'])
      ]

setup(
    ext_modules=cythonize(ext)
)
