#include "DataFrame.hpp"

#include <cctype>
#include <exception>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>

#include "Row.hpp"

using namespace std;

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
            _headers.push_back(header);
        }
    }

    while (getline(file, line)) {
        auto row = parseLine((line));
        for (size_t i = 0; i < headers.size(); ++i) {
            _columns[headers[i]].push_back(row[i]);
        }
    }

    file.close();

    for (auto& col : _columns) {
        col.second.inferType();
    }
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

void DataFrame::describe() const {
    vector<string>        headers = {"Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"};
    vector<string>         features;
    vector<vector<double>> stats(headers.size(), std::vector<double>());

    for (const auto& [header, column] : _columns) {
        if (column.type() == Column::DataType::FLOAT) {
            features.push_back(header.substr(0, 7));
            stats[0].push_back(column.count());
            try {
                stats[1].push_back(column.mean());
            } catch (const exception& e) {
                cerr << e.what() << endl;
            }
            try {
                stats[2].push_back(column.stddev());
            } catch (const exception& e) {
                cerr << e.what() << endl;
            }
            stats[3].push_back(column.min());
            try {
                stats[4].push_back(column.percentile(0.25));
                stats[5].push_back(column.percentile(0.50));
                stats[6].push_back(column.percentile(0.75));
            } catch (const exception& e) {
                cerr << e.what() << endl;
            }
            stats[7].push_back(column.max());
        }
    }

    cout << setw(10) << "";
    for (const auto& feature : features) {
        cout << setw(20) << feature;
    }
    cout << endl;

    for (size_t i = 0; i < headers.size(); ++i) {
        cout << setw(10) << headers[i];
        for (size_t j = 0; j < features.size(); ++j) {
            cout << setw(20) << fixed << setprecision(6) << stats[i][j];
        }
        cout << endl;
    }
}