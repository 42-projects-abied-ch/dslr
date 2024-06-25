from DataFrame import DataFrame
import argparse

def get_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to the CSV file")
    args = parser.parse_args()
    return args

def preprocess_data(df: DataFrame) -> dict:
    df.drop_non_numerical(index=False)
    df.fillna_with_mean()
    df = df.scale_features()
    return df

def get_targets(df: DataFrame) -> list[int]:
    targets = df.get_column("Hogwarts House")._data
    houses = list(set(targets))
    for i in range(len(targets)):
        targets[i] = houses.index(targets[i])
    targets = [[int(x)] for x in targets]
    return targets

def fill_none_with_mean(training_features):
    col_sums = [0] * len(training_features[0])
    col_counts = [0] * len(training_features[0])
    
    for row in training_features:
        for idx, val in enumerate(row):
            if val is not None:
                col_sums[idx] += val
                col_counts[idx] += 1
    
    col_means = [col_sums[i] / col_counts[i] if col_counts[i] > 0 else 0 for i in range(len(col_sums))]
    
    for row in training_features:
        for idx, val in enumerate(row):
            if val is None:
                row[idx] = col_means[idx]
    
    return training_features

def extract_features(df: dict, feature_pairs: list):
    available_features = list(df.keys())
    print("Available features after preprocessing:", available_features)
    training_features = []
    
    for i in range(len(next(iter(df.values())))):
        row_features = []
        for f1, f2 in feature_pairs:
            if f1 in df and f2 in df:
                row_features.append(df.get(f1)[i])
                row_features.append(df.get(f2)[i])
            else:
                print(f"Warning: Feature pair ({f1}, {f2}) contains missing features.")
                row_features.append(None)
                row_features.append(None)
        training_features.append(row_features)
    
    return training_features

def main():
    args = get_arg()
    df = DataFrame()
    df.read_csv(args.path)
    targets = get_targets(df)
    df = preprocess_data(df)
    feature_pairs = [
        ("Astronomy", "Herbology"),
        ("Astronomy", "Ancient Runes"),
        ("Astronomy", "Charms"),
        ("Herbology", "Defence Against the Dark Arts"),
        ("Herbology", "Ancient Runes"),
        ("Defence Against the Dark Arts", "Ancient Runes"),
        ("Defence Against the Dark Arts", "Charms"),
        ("Divination", "Charms")
    ]

    feature_data = extract_features(df, feature_pairs)
    feature_data = fill_none_with_mean(feature_data)
    for i in range(len(feature_data)):
        print(feature_data[i])
        print(targets[i])

if __name__ == "__main__":
    main()