import math
from datetime import datetime

INT = "int"
FLOAT = "float"
STRING = "string"
DATE = "date"
BOOL = "bool"
NONE = "none"


class Column:
    def __init__(self, name, data):
        self._name = name
        self._data = []
        self._type = []

    def _get_type(self, value):
        try:
            int(value)
            return INT
        except ValueError:
            pass

        try:
            float(value)
            return FLOAT
        except ValueError:
            pass

        if value.lower() in ["true", "false"]:
            return BOOL

        try:
            datetime.strptime(value, "%Y-%m-%d")
            return DATE
        except ValueError:
            pass

        if value == "":
            return NONE
        return STRING

    def get_column(self, name):
        return self._columns[name]

    def add_value(self, value):
        current_type = self._get_type(value)
        if current_type == INT:
            self._data.append(int(value))
        elif current_type == FLOAT:
            self._data.append(float(value))
        elif current_type == BOOL:
            self._data.append(value.lower() == "true")
        elif current_type == DATE:
            self._data.append(datetime.strptime(value, "%Y-%m-%d"))
        else:
            self._data.append(value)
        self._type.append(current_type)

    def set_column_name(self, name):
        self.name = name

    def get_column_name(self):
        return self.name

    def get_column_data(self):
        return self._data

    def get_column_data_without_none(self):
        return [x for x in self._data if x != ""]

    def mean(self):
        values = self.get_column_data_without_none()
        result = sum(values) / len(values)
        return round(result, 6)

    def count(self):
        return len(self.get_column_data_without_none())

    def std(self):
        values = self.get_column_data_without_none()
        mean = self.mean()
        result = math.sqrt(sum([(x - mean) ** 2 for x in values]) / (len(values) - 1))
        return round(result, 6)

    def min(self):
        return min(self.get_column_data_without_none())

    def max(self):
        return max(self.get_column_data_without_none())

    def percentile(self, p):
        values = self.get_column_data_without_none()
        values.sort()
        k = (len(values) - 1) * p
        f = math.floor(k)
        c = math.ceil(k)
        if f == c:
            return values[int(k)]
        d0 = values[int(f)] * (c - k)
        d1 = values[int(c)] * (k - f)
        return d0 + d1
