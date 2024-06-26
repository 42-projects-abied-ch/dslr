from DataFrame import DataFrame

if __name__ == '__main__':
    try:
        df = DataFrame()
        df.read_csv('datasets/dataset_train.csv')
        df.histogram_by_houses()
    except Exception as e:
        print(e)