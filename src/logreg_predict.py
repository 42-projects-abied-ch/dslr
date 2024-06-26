from logreg_train import softmax, get_features, LogisticRegression
import numpy as np
import pickle

def predict(X, w, b):
    y_pred_linear = np.dot(X, w) + b
    y_pred = softmax(y_pred_linear)
    class_pred = np.argmax(y_pred, axis=1)
    return class_pred

def main():
    X, y = get_features()
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    w = model.w
    b = model.b
    pred = predict(X, w, b)
    houses_dict = {
        0: "Ravenclaw",
        1: "Slytherin",
        2: "Gryffindor",
        3: "Hufflepuff",
    }
    with open("houses.csv", "w") as file:
        for i in range(len(pred)):
            file.write(f"{i},{houses_dict[pred[i]]}\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)