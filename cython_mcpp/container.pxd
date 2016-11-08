cdef extern from "container.hpp" namespace "mcpp" nogil:
    #Use case: T is a unique_ptr, or other move-only type
    void emplace_object_move[CONTAINER,TYPE](CONTAINER &c, TYPE & t)
    #c.push_back(std::move(t))
    void push_back_move[CONTAINER,TYPE](CONTAINER &c,TYPE &t)
    #c.push_front(std::move(t))
    void push_front_move[CONTAINER,TYPE](CONTAINER &c,TYPE &t)
