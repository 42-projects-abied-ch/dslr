import pandas as pd

def test():
    df = pd.read_csv("datasets/dataset_test.csv")
    df = df.fillna(0)
    print(df.describe())

test()