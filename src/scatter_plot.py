from DataFrame import DataFrame
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt


import numpy as np
import matplotlib.pyplot as plt

def scatter_plot(df):
    df.drop_non_numerical(index=False)
    scaled = df.scale_features()
    headers = list(scaled.keys())

    for i, x_header in enumerate(headers):
        for y_header in headers[i + 1:]:
            x = np.array(scaled[x_header])
            y = np.array(scaled[y_header])

            mask = (x != 0) & (y != 0)
            filtered_x = x[mask]
            filtered_y = y[mask]

            plt.scatter(filtered_x, filtered_y, color="tab:blue", label=f"{x_header} (x)", alpha=0.5)
            plt.scatter(filtered_x, filtered_y, color="tab:orange", label=f"{y_header} (y)", alpha=0.1)

            plt.xlabel(x_header)
            plt.ylabel(y_header)
            plt.title(f"{x_header} vs {y_header}")
            plt.legend(loc="upper right")
            plt.show()


def main():
    df = DataFrame()
    df.read_csv("datasets/dataset_train.csv")
    scatter_plot(df)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
