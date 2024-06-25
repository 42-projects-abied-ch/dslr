import csv
import tabulate
from Column import Column
from Row import Row
import datetime

class DataFrame:
    def __init__(self):
        self._columns = {}
        self._rows = []
    
    def add_column(self, name, data):
        self._columns[name] = Column(name, data)
    
    def get_column(self, name):
        return self._columns[name]

    def read_csv(self, path):
        with open(path) as file:
            reader = csv.reader(file)
            header = next(reader)
            for column in header:
                self.add_column(column, [])
            for row in reader:
                for column, value in zip(header, row):
                    self.get_column(column).add_value(value)
                self._rows.append(Row(header, row))
    
    def describe(self):
        description = {}
        for header in self._columns:
            if header == 'Index':
                continue
            if isinstance(self._columns[header].get_column_data()[0], str):
                continue
            if isinstance(self._columns[header].get_column_data()[0], datetime.datetime):
                continue
            description[header] = {
                'Count' : self._columns[header].count(),
                'Mean' : self._columns[header].mean(),
                'Std' : self._columns[header].std(),
                'Min' : self._columns[header].min(),
                '25%' : self._columns[header].percentile(0.25),
                '50%' : self._columns[header].percentile(0.50),
                '75%' : self._columns[header].percentile(0.75),
                'Max' : self._columns[header].max()
            }
        return description
    
    def drop_non_numerical(self):
        pop = []
        for header in self._columns:
            if isinstance(self._columns[header].get_column_data()[0], str):
                pop.append(header)
            elif isinstance(self._columns[header].get_column_data()[0], datetime.datetime):
                pop.append(header)
        for header in pop:
            self._columns.pop(header)

    def print_describe(self):
        description = self.describe()
        table_data = list(map(list, zip(*[(k, *[format(val, '.6f') for val in v.values()]) for k, v in description.items()])))
        headers = ['Feature', 'Count', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max']
        for i in range(len(table_data)):
            table_data[i].insert(0, headers[i])
        print(tabulate.tabulate(table_data, tablefmt='pretty'))