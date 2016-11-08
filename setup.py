#!/usr/bin/env python
from distutils.core import setup
import glob
setup(
    name="cython_mcpp",
    version="0.0.1",
    author="Kevin R. Thornton",
    author_email="krthornt@uci.edu",
    url="http://github.com/molpopgen/cython_mcpp",
    packages=["cython_mcpp"],
    package_data={"cython_mcpp": ["*.pxd"]},
    description="""Glue between Cython and C++11/14/17""",
    setup_requires=['Cython >= 0.25'],
    install_requires=['Cython >= 0.25'],
    headers=glob.glob("include/*.hpp"),
    classifiers=[
                'Development Status :: 4 - Beta',
                'Environment :: Console',
                'Operating System :: OS Independent',
                'Intended Audience :: Science/Research',
                'License :: OSI Approved :: GNU General Public License (GPL)',
                'Programming Language :: Python',
                'Topic :: Scientific/Engineering']
)
