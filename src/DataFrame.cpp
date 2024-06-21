#include "DataFrame.hpp"

#include <fstream>
#include <sstream>

#include "Row.hpp"

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

void DataFrame::readCSV(const string& path) {
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
