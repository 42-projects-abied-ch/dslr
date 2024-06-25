from DataFrame import DataFrame
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def scatter_plot(df):
    df.drop_non_numerical(index=False)  # Assuming this function properly cleans the DataFrame
    headers = list(df._columns.keys())
    
    for i, x_header in enumerate(headers):
        for y_header in headers[i+1:]:
            x_data = df._columns[x_header].get_column_data()
            y_data = df._columns[y_header].get_column_data()

            # Plot x_data points in blue
            plt.scatter(x_data, [0]*len(x_data), color='blue', label=x_header)  # Plotting at y=0 for visualization
            
            # Plot y_data points in red
            plt.scatter(y_data, [1]*len(y_data), color='red', label=y_header)  # Plotting at y=1 for visualization
            
            # Adding labels and titles
            plt.xlabel(x_header)
            plt.ylabel(y_header)
            plt.title(f'{x_header} vs {y_header}')
            plt.legend()
            plt.show()

def main():
    df = DataFrame()
    df.read_csv("datasets/dataset_train.csv")
    scatter_plot(df)

if __name__ == "__main__":
    main()