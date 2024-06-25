from DataFrame import DataFrame
from Column import Column
import pandas as pd
import numpy as np


if __name__ == '__main__':
    df = DataFrame()
    df.read_csv('../datasets/dataset_train.csv')
    df.print_describe()
    df.scale_features()
    # Pandas describe to compare
    # pd.set_option('display.max_columns', None)
    # pd_df = pd.read_csv('../datasets/dataset_test.csv')
    # print(pd_df.describe())