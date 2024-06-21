#ifndef COLUMN_HPP
#define COLUMN_HPP

#include <string>
#include <vector>

using namespace std;

class Column {
public:
    void          push_back(const string &cell) { _data.push_back(cell); }
    float         count() { return _data.size(); }
    const string &at(size_t index) const { return _data.at(index); }

    bool isNumerical() const;

private:
    vector<string> _data;
};

#endif  //  COLUMN_HPP