#include <utility>
#include <memory>
#include <vector>

namespace mcpp
{
    template <typename T, template <typename> allocator = std::allocator<T>>
    void
    emplace_back_move(std::vector<T, allocator> &v, T &t)
    {
        v.emplace_back(std::move(t));
    }
}
