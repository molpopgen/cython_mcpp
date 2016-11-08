#This file is a modification of setup_tests.py
#from the Cython GSL project 
#(https://github.com/twiecki/CythonGSL) by
#Thomas Wiecki
from distutils.core import setup
from Cython.Distutils import Extension
from Cython.Distutils import build_ext
from glob import glob
import os.path
import cython_mcpp
from os.path import splitext

ext_modules = []
GLOBAL_INCLUDES=['.','..','../../include','include','../include']
STANDARD="-std=c++11"
for pyxfile in glob(os.path.join('cython_mcpp', 'test', '*.pyx')):
    ext_name = splitext(os.path.split(pyxfile)[-1])[0]
    print ext_name
    ext = Extension('cython_mcpp.test.'+ext_name,
                    [pyxfile],
                    language="c++",
                    extra_compile_args=[STANDARD],  
                    include_dirs=GLOBAL_INCLUDES)
    ext_modules.append(ext)

setup(
    name="cython_mcpp_test",
    version="0.0.1",
    author="Kevin R Thornton",
    author_email="krthornt@uci.edu",
    url="http://github.com/molpopgen/cython_mcpp",
    packages=["cython_mcpp.test"],
    package_data={"cython_mcpp.test": ["*.py"]},
    description="""Glue between Cython and C++11/14/17""",
    setup_requires=['Cython >= 0.25',],
    install_requires=['Cython >= 0.25',],
    classifiers=[
                'Development Status :: 4 - Beta',
                'Environment :: Console',
                'Operating System :: OS Independent',
                'Intended Audience :: Science/Research',
                'License :: OSI Approved :: GNU General Public License (GPL)',
                'Programming Language :: Python',
                'Topic :: Scientific/Engineering'],
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
