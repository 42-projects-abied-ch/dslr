import csv
import tabulate
from Column import Column
from Row import Row
import datetime
import matplotlib.pyplot as plt

RAVENCLAW = 'Ravenclaw'
SLYTHERIN = 'Slytherin'
HUFFLEPUFF = 'Hufflepuff'
GRYFFINDOR = 'Gryffindor'

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
            if header == "Index":
                continue
            if isinstance(self._columns[header].get_column_data()[0], str):
                continue
            if isinstance(
                self._columns[header].get_column_data()[0], datetime.datetime
            ):
                continue
            description[header] = {
                "Count": self._columns[header].count(),
                "Mean": self._columns[header].mean(),
                "Std": self._columns[header].std(),
                "Min": self._columns[header].min(),
                "25%": self._columns[header].percentile(0.25),
                "50%": self._columns[header].percentile(0.50),
                "75%": self._columns[header].percentile(0.75),
                "Max": self._columns[header].max(),
            }
        return description

    def drop_non_numerical(self, index: bool = True):
        if not index:
            self._columns.pop("Index")
        pop = []
        for header in self._columns:
            if isinstance(self._columns[header].get_column_data()[0], str):
                pop.append(header)
            elif isinstance(
                self._columns[header].get_column_data()[0], datetime.datetime
            ):
                pop.append(header)
        for header in pop:
            self._columns.pop(header)
        for header in self._columns:
            self._columns[header]._data = [
                float(x) if x != "" else 0.0 for x in self._columns[header]._data
            ]

    def scale_features(self) -> None:
        normilized_data = {}
        for key, column in self._columns.items():
            mean = column.mean()
            std = column.std()
            normilized_data[key] = [
                (x - mean) / std for x in column.get_column_data_without_none()
            ]
        return normilized_data

    def print_describe(self):
        description = self.describe()
        table_data = list(
            map(
                list,
                zip(
                    *[
                        (k, *[format(val, ".6f") for val in v.values()])
                        for k, v in description.items()
                    ]
                ),
            )
        )
        headers = ["Feature", "Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]
        for i in range(len(table_data)):
            table_data[i].insert(0, headers[i])
        print(tabulate.tabulate(table_data, tablefmt='pretty'))
    
    def scale_features(self) -> None:
        """
        Standardize the features for faster convergence.
        """
        normilized_data = {}
        for key, column in self._columns.items():
            if isinstance(column.get_column_data_without_none()[0], str):
                continue
            if isinstance(column.get_column_data_without_none()[0], datetime.datetime):
                continue
            mean = column.mean()
            std = column.std()
            normilized_data[key] = [(x - mean) / std for x in column.get_column_data_without_none()]
        return normilized_data

    def get_rows_by_house(self, house):
        return [row for row in self._rows if row.get_value('Hogwarts House') == house]
    
    def histogram_by_houses(self):
        data = {}
        num_columns = self.get_numerical_columns()
        for column in num_columns:
            data[column] = {
                RAVENCLAW : [],
                SLYTHERIN : [],
                HUFFLEPUFF : [],
                GRYFFINDOR : []
            }
        for house in [RAVENCLAW, SLYTHERIN, HUFFLEPUFF, GRYFFINDOR]:
            rows = self.get_rows_by_house(house)
            for column in num_columns:
                data[column][house] = [float(row.get_value(column)) for row in rows if row.get_value(column) != '']
        for column in num_columns:
            if column == 'Index':
                continue
            fig, ax = plt.subplots()
            ax.hist(data[column][RAVENCLAW], bins=20, alpha=0.5, label=RAVENCLAW, color='blue')
            ax.hist(data[column][SLYTHERIN], bins=20, alpha=0.5, label=SLYTHERIN, color='green')
            ax.hist(data[column][HUFFLEPUFF], bins=20, alpha=0.5, label=HUFFLEPUFF, color='yellow')
            ax.hist(data[column][GRYFFINDOR], bins=20, alpha=0.5, label=GRYFFINDOR, color='red')
            ax.set_xlabel(column)
            ax.set_ylabel('Frequency')
            ax.set_title(column)
            ax.legend(loc='upper right')
            plt.show()
    
    def pair_plot(self):
        data = {}
        num_columns = self.get_numerical_columns()
        num_columns.remove('Index')
        for column in num_columns:
            data[column] = {
                RAVENCLAW : [],
                SLYTHERIN : [],
                HUFFLEPUFF : [],
                GRYFFINDOR : []
            }
        for house in [RAVENCLAW, SLYTHERIN, HUFFLEPUFF, GRYFFINDOR]:
            rows = self.get_rows_by_house(house)
            for column in num_columns:
                data[column][house] = [float(row.get_value(column)) if row.get_value(column) != '' else float('nan') for row in rows]
        for i in range(len(num_columns)):
            for j in range(i + 1, len(num_columns)):
                fig, ax = plt.subplots()
                ax.scatter(data[num_columns[i]][RAVENCLAW], data[num_columns[j]][RAVENCLAW], color='blue', label=RAVENCLAW)
                ax.scatter(data[num_columns[i]][SLYTHERIN], data[num_columns[j]][SLYTHERIN], color='green', label=SLYTHERIN)
                ax.scatter(data[num_columns[i]][HUFFLEPUFF], data[num_columns[j]][HUFFLEPUFF], color='yellow', label=HUFFLEPUFF)
                ax.scatter(data[num_columns[i]][GRYFFINDOR], data[num_columns[j]][GRYFFINDOR], color='red', label=GRYFFINDOR)
                ax.set_xlabel(num_columns[i])
                ax.set_ylabel(num_columns[j])
                ax.set_title(f'{num_columns[i]} vs {num_columns[j]}')
                ax.legend(loc='upper right')
                plt.show()
        