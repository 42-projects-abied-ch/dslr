#ifndef ROW_HPP
#define ROW_HPP

#include <string>
#include <vector>

using namespace std;

class Row {
public:
    void          push_back(const std::string &cell) { _data.push_back(cell); }
    size_t        size() const { return _data.size(); }
    auto          begin() { return _data.begin(); }
    auto          end() { return _data.end(); }
    const string &operator[](int64_t index);

private:
    vector<string> _data;
};

#endif  //  ROW_HPP