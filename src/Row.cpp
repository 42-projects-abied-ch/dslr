#include "Row.hpp"

#include <stdexcept>

const string& Row::operator[](int64_t index) {
    if (index < 0) {
        index = _data.size() + index;
    }
    if (index < 0 || index >= _data.size()) {
        throw out_of_range("Index out of range");
    }
    return _data[index];
}