#include "Column.hpp"

#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <limits>
#include <sstream>
#include <string>

bool Column::isFloat(const string& s) const {
    char* end = nullptr;
    strtod(s.c_str(), &end);
    return s == "none" || end != s.c_str() && *end == '\0';
}

bool Column::isBoolean(const string& s) const {
    string lower_s;
    std::transform(s.begin(), s.end(), std::back_inserter(lower_s), ::tolower);
    return s == "none" || lower_s == "true" || lower_s == "false";
}

bool Column::isDateTime(const string& s) const {
    tm            tm = {};
    istringstream ss(s);
    ss >> get_time(&tm, "%Y-%m-%d");
    return s == "none" || !ss.fail();
}

void Column::inferType() {
    _inferredType = DataType::STRING;

    for (const auto& value : _data) {
        if (isFloat(value)) {
            _inferredType = DataType::FLOAT;
        } else if (isBoolean(value)) {
            _inferredType = DataType::BOOL;
        } else if (isDateTime(value)) {
            _inferredType = DataType::DATETIME;
        } else {
            _inferredType = DataType::STRING;
            break;
        }
    }
    if (_inferredType == DataType::FLOAT) {
        convertFloatType();
    }
}

void Column::convertFloatType() {
    _floatData.reserve(_data.size());

    for (const auto& s : _data) {
        if (s == "none") {
            _floatData.push_back(numeric_limits<double>::quiet_NaN());
        } else {
            _floatData.push_back(strtod(s.c_str(), nullptr));
        }
    }
}
