#!/usr/bin/env python

from __future__ import print_function
from distutils.core import setup, Extension
#@CYTHONIMPORT@
import platform, glob, sys, subprocess, os

#Are we gonna build using Cython or not?  Default is not to,
#which allows us to ship this in a standard way.
if '--use-cython' in sys.argv:
    USE_CYTHON = True
    sys.argv.remove('--use-cython')
else:
    USE_CYTHON = False


long_desc = open("README.rst").read()

#EXTENSION = '.pyx' if USE_CYTHON else '.cpp'

extensions=[]
provided=[]
pdata={'cython_mcpp':['*.pxd']}
modules=['vector']

STANDARD="-std=c++11"
GLOBAL_INCLUDES=['.','..','include']
for i in modules:
    extensions.append(Extension("cython_mcpp."+i,
                                sources=[],
#                                sources=["cython_mcpp/"+i+EXTENSION],
                                include_dirs=GLOBAL_INCLUDES,
                                language="c++",                  
                                extra_compile_args=[STANDARD],  
                                extra_link_args=[STANDARD],))
    provided.append('cython_mcpp.'+i)

#If using Cython, edit extensions here:
if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)

setup(name='cython_mcpp',
      version='0.0.1',
      author='Kevin R. Thornton',
      author_email='krthornt@uci.edu',
      maintainer='Kevin R. Thornton',
      maintainer_email='krthornt@uci.edu',
      url='http://github.com/molpopgen/cython_mcpp',
      description="Glue between Cython and C++11/14/17",
      long_description=long_desc,
      data_files=[('cython_mcpp', ['COPYING', 'README.rst'])],
      download_url='',
      classifiers=[],
      platforms=['Linux','OS X'],
      license='GPL >= 2',
      provides=provided,
      obsoletes=['none'],
      packages=['libsequence'],
      py_modules=[],
      scripts=[],
      package_data=pdata,
      ##Note: when installing the git repo, headers will be put somewhere like /usr/local/include/pythonVERSION/fwdpy
      headers=glob.glob("include/*.hpp"),
      ext_modules=extensions
)

