#ifndef FROG_HPP
#define FROG_HPP

#include <string>
#include <unordered_map>
#include <vector>

using namespace std;
typedef vector<string> Row;

class Column {
public:
    void push_back(const string& cell) { data.push_back(cell); }

    size_t count() { return data.size(); }

    const string& at(size_t index) const { return data.at(index); }

private:
    vector<string> data;
};

class DataFrame {
public:
    DataFrame(const string& path) { loadCSV(path); }

    Column& operator[](const string& columnName);

    Row operator[](size_t rowIndex) const;

private:
    unordered_map<string, Column> _columns;

    void loadCSV(const string& path);

    Row parseLine(const string& line) const;

    DataFrame() = default;
};

#endif  //  FROG_HPP