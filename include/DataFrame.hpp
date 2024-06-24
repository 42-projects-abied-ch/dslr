#ifndef DATAFRAME_HPP
#define DATAFRAME_HPP

#include <cstddef>
#include <string>
#include <unordered_map>
#include <vector>
#include <matplot/matplot.h>

#include "Column.hpp"

using namespace std;

class Row;

class DataFrame {
public:
    DataFrame(const string &path) { readCSV(path); }
    Column        &operator[](const string &columnName);
    Row            operator[](size_t rowIndex) const;
    vector<string> headers() const { return _headers; }
    void           describe() const;

private:
    unordered_map<string, Column> _columns;
    vector<string>                _headers;

    void readCSV(const string &path);
    Row  parseLine(const string &line) const;

    DataFrame() = default;
};

#endif  //  DATAFRAME_HPP