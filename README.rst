"Glue" for Cython_ and modern C++
==============================================

This package provides support for move-only C++ objects in Cython_.  For example, vectors of unique_ptr are currently difficult to work with in Cython_, due to the lack of support for move semantics.

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

   extensions=["name",
               language="c++",
               include_dirs=[cython_mcpp.get_includes()],
               extra_compile_args=['-std=c++11']]

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

For examples, see the unit test container_unit_tests.pyx.  This function is *generic*, and works for any STL container type supporting emplacement.

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

See the unit test container_unit_tests.pyx for examples of using these functions for specific tasks.

.. _Cython: http://www.cython.org/
