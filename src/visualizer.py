# visualizer.py
import matplotlib.pyplot as plt


def plot_misclassifications(ppn):
    plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Number of misclassifications')
    plt.show()


def visualize_data(X, y):
    plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='Setosa')
    plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='Versicolor')
    plt.xlabel('Sepal Length')
    plt.ylabel('Petal Length')
    plt.legend(loc='upper left')
    plt.show()
