from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'sort cython',
  ext_modules = cythonize("*.pyx"),
)