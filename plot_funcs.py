from typing import List
import numpy as np
import matplotlib.pyplot as plt


def vector_plotter(vectors: List, colors: List, alpha=1):
    """
    Returns Vectors plots.
    :param vectors: Vectors.
    :param colors: List of Colors.
    :param alpha: Transparency Level.
    :return: Vector Plots.
    """
    plt.axvline(x=0, color="grey", zorder=0, linestyle="--")
    plt.axhline(y=0, color="grey", zorder=0, linestyle="--")
    for i in range(len(vectors)):
        x = np.concatenate([[0, 0], vectors[i]])
        plt.quiver([x[0]], [x[1]], [x[2]], [x[3]],
                   angles="xy", scale_units="xy",
                   scale=1, color=colors[i], alpha=alpha)


def matrix_plotter(matrix, vector_colors: List):
    """
    Returns a Unitary Circle and the Vectors.
    :param matrix: Matrix
    :param vector_colors: List of Colors.
    :return: Circle and Vectors Plots.
    """
    x = np.linspace(-1, 1, 100000)
    y = np.sqrt(1-x**2)
    # Unitary Circle.
    x1 = matrix[0, 0] * x + matrix[0, 1] * y
    y1 = matrix[1, 0] * x + matrix[1, 1] * y
    # Transformed Unitary Circle.
    x1_negative = matrix[0, 0] * x - matrix[0, 1] * y
    y1_negative = matrix[1, 0] * x - matrix[1, 1] * y
    # Vectors.
    u1 = [matrix[0, 0], matrix[1, 0]]
    v1 = [matrix[0, 1], matrix[1, 1]]
    vector_plotter(vectors=[u1, v1], colors=[vector_colors[0], vector_colors[1]])
    plt.plot(x1, y1, "#08415C", alpha=0.7)
    plt.plot(x1_negative, y1_negative, "#08415C", alpha=0.7)
