#include "Column.hpp"

#include <cmath>
#include <cstddef>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <limits>
#include <sstream>
#include <stdexcept>
#include <string>

bool Column::isFloat(const string& s) const {
    char* end = nullptr;
    strtod(s.c_str(), &end);
    return s == "none" || end != s.c_str() && *end == '\0';
}

bool Column::isBoolean(const string& s) const {
    string lower_s;
    std::transform(s.begin(), s.end(), back_inserter(lower_s), ::tolower);
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

double Column::mean() const {
    if (_inferredType != DataType::FLOAT) {
        throw runtime_error("Cannot compute mean of non-float column");
    }
    double sum = 0.0;
    size_t count = 0;

    for (const auto& value : _floatData) {
        if (!isnan(value)) {
            sum += value;
            ++count;
        }
    }
    return double(sum / (double)count);
}

double Column::stddev() const {
    double meanVal = mean();
    double accumulation = 0.0;
    size_t count = 0;

    for (const auto& val : _floatData) {
        if (!isnan(val)) {
            accumulation += (val - meanVal) * (val - meanVal);
            ++count;
        }
    }
    if (count < 2) {
        throw runtime_error("Standard deviation requires at least two data points");
    }
    return sqrt(accumulation / static_cast<double>(count - 1));
}

double Column::min() const {
    double minVal = numeric_limits<double>::infinity();
    for (const auto& val : _floatData) {
        if (!isnan(val) && val < minVal) {
            minVal = val;
        }
    }
    return minVal;
}

double Column::max() const {
    double maxVal = -numeric_limits<double>::infinity();
    for (const auto& val : _floatData) {
        if (!isnan(val) && val > maxVal) {
            maxVal = val;
        }
    }
    return maxVal;
}

double Column::percentile(double p) const {
    vector<double> sortedVals;
    for (const auto& val : _floatData) {
        if (!isnan(val)) {
            sortedVals.push_back(val);
        }
    }
    if (sortedVals.empty()) {
        throw runtime_error("Cannot compute percentile of empty column");
    }
    sort(sortedVals.begin(), sortedVals.end());
    size_t n = sortedVals.size();
    double rank = p * (n - 1);
    size_t low = static_cast<size_t>(floor(rank));
    size_t high = static_cast<size_t>(ceil(rank));
    double weight = rank - low;
    return sortedVals[low] * (1 - weight) + sortedVals[high] * weight;
}