#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

libbcm2835_extionsion = Extension(
    name="bcm2835_wrap",
    sources=["bcm2835_wrap.pyx"],
    libraries=["bcm2835"],
    library_dirs=["libbcm2835"],
    include_dirs=["libbcm2835"]
)

setup(
    name="bcm2835_wrap",
    ext_modules=cythonize([libbcm2835_extionsion])
)
