#ifndef FROG_HPP
#define FROG_HPP

#include <cstddef>
#include <cstdint>
#include <string>
#include <unordered_map>
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

class Column {
public:
    void push_back(const string &cell) { _data.push_back(cell); }

    float         count() { return _data.size(); }
    const string &at(size_t index) const { return _data.at(index); }

    bool isNumerical() const;

private:
    vector<string> _data;
};

class DataFrame {
public:
    DataFrame(const string &path) { loadCSV(path); }

    Column &operator[](const string &columnName);

    Row operator[](size_t rowIndex) const;

private:
    unordered_map<string, Column> _columns;

    void loadCSV(const string &path);

    Row parseLine(const string &line) const;

    DataFrame() = default;
};

#endif  //  FROG_HPP