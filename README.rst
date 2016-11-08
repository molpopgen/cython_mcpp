"Glue" for Cython_ and modern C++
==============================================

This package provides support for move-only C++ objects in Cython_.  For example, vectors of unique_ptr are currently difficult to work with in Cython_, due to the lack of support for move semantics.

Build status
==========================================

Master branch:

.. image:: https://travis-ci.org/molpopgen/cython_mcpp.svg?branch=master
   :target: https://travis-ci.org/molpopgen/cython_mcpp
   :alt: Travis CI Build Status (master branch)

License
================================

setup.py and setup_tests.py are both GPL >= 2.  They were copied from files of the same name found in the CythonGSL_ project, which is GPL.

The rest of the package, including all code, is under the Apache license, as is Cython_. See COPYING or LICENSE.txt for details.

Installation
=================================

.. code-block:: python

   python setup.py install
   #or
   python setup.py install --user
   #or
   pip install .

Running the unit tests
=================================

.. code-block:: python

   python setup_tests.py build_ext -i
   python -m unittest discover cython_mcpp/test

Including the header files into your own project:
==================================

.. note:: This only works (has been tested on...) POSIX systems.

Use the following code in your setup.py:

.. code-block:: python

   import cython_mcpp
   from Cython.Distutils import Extension

   extensions=[Extension("name",
               language="c++",
               include_dirs=[cython_mcpp.get_includes()],
               extra_compile_args=['-std=c++11'])]

Modules provided
-----------------------------

container
+++++++++++++++++++++++++++++

.. code-block:: cython
   
   from cython_mcpp.container cimport *

Functions provided:

.. code-block:: cython
   
   #Use std::move to emplace or emplace_back t into v.
   #SFINAE is used to determine emplace vs emplace_back.
   void emplace_object_move[CONTAINER,TYPE](CONTAINER & v, TYPE & t)
   #c.push_back(std::move(t))
   void push_back_move[CONTAINER,TYPE](CONTAINER &c,TYPE &t)
   #c.push_front(std::move(t))
   void push_front_move[CONTAINER,TYPE](CONTAINER &c,TYPE &t)
   #c.emplace(p,std::move(t))
   POS emplace_object_pos_move[CONTAINER,POS,TYPE](CONTAINER &c,POS p,TYPE &t)

For examples, see the unit test container_unit_tests.pyx.  These function are *generic*, and work for any container supporting these operations.

The unit tests also illustrate cases where casts are needed in order that either the Cython code in the .pyx file or the generated C++ code compile.

The back-end of emplace_object_move uses variadic templates.  You may expose these variadics to Cython in order to use "emplacement" as intended, which is with constructor arguments as parameters.  The relevant functions are:

.. code-block:: cpp
    
   template <typename container, typename... args>
   inline auto
   emplace(container &c, args &&... Args)
       -> decltype(detail::emplace_dispatch(c, std::forward<args>(Args)...))
   {
       return detail::emplace_dispatch(c, std::forward<args>(Args)...);
   }

   template <typename container, typename... args>
   inline auto
   emplace_move(container &c, args &&... Args)
        -> decltype(emplace(c, std::move(Args)...))
   {
       return emplace(c, std::move(Args)...);
   }

Likewise, emplacement via move at a position is supported:

.. code-block:: cpp

   template <typename container, typename pos, typename... args>
   inline auto
   emplace_pos_move(container &v, pos p, args &&... Args)
       -> decltype(v.emplace(p, std::forward<args>(Args)...))
   {
       return v.emplace(p, std::forward<args>(Args)...);
   }

See the unit test container_unit_tests.pyx for examples of using these functions for specific tasks.

.. _Cython: http://www.cython.org/
.. _CythonGSL: https://github.com/twiecki/CythonGSL
