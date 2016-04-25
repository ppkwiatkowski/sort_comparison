from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

ext = [Extension('cy_swenson_sort', ['cy_swenson_sort.pyx', 'swenson_sort.c']),
       #Extension('cy_cubesort', ['cy_cubesort.pyx', 'cubesort.c']),
       Extension('cy_smoothsort', ['cy_smoothsort.pyx', 'smoothsort.c']),
       Extension('cy_introsort', ['cy_introsort.pyx', 'introsort.c'])]

setup(
    ext_modules=cythonize(ext)
)
