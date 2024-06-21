#include "Frog.hpp"

#include <cstdint>
#include <fstream>
#include <sstream>

Column& DataFrame::operator[](const string& columnName) {
    auto it = _columns.find(columnName);
    if (it == _columns.end()) {
        throw invalid_argument("Column not found: " + columnName);
    }
    return it->second;
}

Row DataFrame::operator[](size_t rowIndex) const {
    Row row;
    for (const auto& col : _columns) {
        row.push_back(col.second.at(rowIndex));
    }
    return row;
}

void DataFrame::loadCSV(const string& path) {
    ifstream file(path);
    if (!file.is_open()) {
        throw runtime_error("Could not open file: " + path);
    }

    string line;
    Row    headers;

    if (getline(file, line)) {
        headers = parseLine(line);
        for (const auto& header : headers) {
            _columns[header] = Column();
        }
    }

    while (getline(file, line)) {
        auto row = parseLine((line));
        for (size_t i = 0; i < headers.size(); ++i) {
            _columns[headers[i]].push_back(row[i]);
        }
    }

    file.close();
}

Row DataFrame::parseLine(const string& line) const {
    stringstream ss(line);
    string       cell;
    Row          row;

    while (getline(ss, cell, ',')) {
        if (cell.empty()) {
            row.push_back("none");
        } else {
            row.push_back(cell);
        }
    }
    return row;
}

const string& Row::operator[](int64_t index) {
    if (index < 0) {
        index = _data.size() + index;
    }
    if (index < 0 || index >= _data.size()) {
        throw out_of_range("Index out of range");
    }
    return _data[index];
}