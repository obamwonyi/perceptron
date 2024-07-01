# main.py
from src.data_loader import load_data
from src.model_trainer import train_model
from src.visualizer import plot_misclassifications, visualize_data
from src.perceptron import Perceptron


def main():
    # Load the data
    X, y = load_data()

    # Train the model
    ppn = train_model(X, y)

    # Plot misclassifications
    plot_misclassifications(ppn)

    # Visualize the data
    visualize_data(X, y)


if __name__ == "__main__":
    main()
