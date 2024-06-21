#ifndef COLUMN_HPP
#define COLUMN_HPP

#include <string>
#include <vector>

using namespace std;

class Column {
public:
    void                  push_back(const string& cell) { _data.push_back(cell); }
    float                 count() { return _data.size(); }
    const string&         at(size_t index) const { return _data.at(index); }
    const vector<string>& getData() const { return _data; }

    enum DataType { FLOAT, BOOL, STRING, DATETIME };
    void     inferType();
    DataType dType() const { return _inferredType; }

private:
    bool isBoolean(const string& s) const;
    bool isFloat(const string& s) const;
    bool isDateTime(const string& s) const;

    vector<string> _data;
    DataType       _inferredType = DataType::STRING;
};

#endif  //  COLUMN_HPP