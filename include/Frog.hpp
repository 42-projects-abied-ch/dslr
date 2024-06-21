#ifndef FROG_HPP
#define FROG_HPP

#include <string>
#include <unordered_map>
#include <vector>


using namespace std;
typedef vector<string> Column;
typedef vector<string> Row;

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