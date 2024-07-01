# data_loader.py

from sklearn.datasets import load_iris
import numpy as np


def load_data():
    iris = load_iris()
    X = iris.data[:100, [0, 2]]  # sepal length, petal length
    y = iris.target[:100]
    y = np.where(y == 0, -1, 1)  # Setosa = -1, Versicolor = 1
    return X, y
