class Row:
    def __init__(self, headers, row):
        self._data = {}
        for header, value in zip(headers, row):
            self._data[header] = value
    
    def get_value(self, header):
        return self._data[header]
    
    def get_values(self):
        return self._data
    
    def get_headers(self):
        return self._data.keys()
    
    def get_data(self):
        return self._data