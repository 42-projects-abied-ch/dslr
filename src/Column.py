INT = 'int'
FLOAT = 'float'
STRING = 'string'
DATE = 'date'
BOOL = 'bool'
NONE = 'none'

class Column:
    def __init__(self, name, data):
        self._name = name
        self._data = []
        self._type = []

    def _get_type(self):
        try:
            int(self.data)
            return INT
        except ValueError:
            pass

        try:
            float(self.data)
            return FLOAT
        except ValueError:
            pass

        if self.data.lower() in ['true', 'false']:
            return BOOL
        
        try:
            datetime.strptime(self.data, '%Y-%m-%d')
            return DATE
        except ValueError:
            pass

        if self.data == '':
            return NONE
        return STRING  
    
    def add_value(self, value):
        self.type.append(self._get_type())
        current_type = self._get_type()
        if current_type == INT:
            self.data.append(int(value))
        elif current_type == FLOAT:
            self.data.append(float(value))
        elif current_type == BOOL:
            self.data.append(value.lower() == 'true')
        elif current_type == DATE:
            self.data.append(datetime.strptime(value, '%Y-%m-%d'))
        else:
            self.data.append(value)
    
    def set_column_name(self, name):
        self.name = name
    
    def get_column_name(self):
        return self.name
    
    def get_column_data(self):
        return self.data
    
    def get_column_data_without_none(self):
        return [x for x in self.data if x != '']