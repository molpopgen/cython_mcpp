from libcpp.vector cimport vector

cdef extern from "vector.hpp" namespace "mcpp" nogil:
    #call v.emplace_back(std::move(t))
    void emplace_back_move[T,ALLOCATOR=*](vector[T,ALLOCATOR] & v, T & t)
