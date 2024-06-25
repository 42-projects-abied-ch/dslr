from DataFrame import DataFrame
import argparse

def get_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to the CSV file")
    args = parser.parse_args()
    return args

def preprocess_data(df: DataFrame) -> DataFrame:
    df.drop_non_numerical(index=False)
    df = df.scale_features()

def get_targets(df: DataFrame) -> list[int]:
    targets = df.get_column("Hogwarts House")._data
    houses = list(set(targets))
    for i in range(len(targets)):
        targets[i] = houses.index(targets[i])
    targets = [[int(x)] for x in targets]
    return targets

def main():
    args = get_arg()
    df = DataFrame()
    df.read_csv(args.path)
    targets = get_targets(df)
    print(targets)
    df = preprocess_data(df)

if __name__ == "__main__":
    main()