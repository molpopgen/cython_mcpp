cdef extern from "container.hpp" namespace "mcpp" nogil:
    #Use case: T is a unique_ptr, or other move-only type
    void emplace_object_move[CONTAINER,TYPE](CONTAINER & v, TYPE & t)
