#ifndef CYTHON_MCPP_CONTAINER_HPP_
#define CYTHON_MCPP_CONTAINER_HPP_

#include <utility>
#include "container_detail.hpp"

namespace mcpp
{
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

    template <typename container, typename type>
    inline auto
    emplace_object_move(container &v, type &t) -> decltype(emplace_move(v, t))
    {
        return emplace_move(v, t);
    }
}

#endif
