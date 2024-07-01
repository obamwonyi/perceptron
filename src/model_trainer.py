# model_trainer.py

from src.perceptron import Perceptron


def train_model(X, y, learning_rate=0.1, n_iter=10):
    ppn = Perceptron(learning_rate=learning_rate, n_iter=n_iter)
    ppn.fit(X, y)
    return ppn
