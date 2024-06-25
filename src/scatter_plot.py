from DataFrame import DataFrame
import matplotlib.pyplot as plt

def scatter_plot(df: DataFrame) -> None:
    df.drop_non_numerical()
    df.print_describe()
    for header in df._columns:
        plt.scatter(df._columns[header].get_column_data(), df._columns[header].get_column_data())
        plt.title(header)
        plt.show

def main():
    df = DataFrame()
    df.read_csv("datasets/dataset_train.csv")
    scatter_plot(df)

if __name__ == "__main__":
    main()