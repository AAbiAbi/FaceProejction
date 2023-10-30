import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from geometry import project_point, rotate_x, rotate_y, rotate

# Your rotation functions go here
# ...

# Example vertices for a cube
vertices = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1],
]
indices = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7],
]

def plot_cube(vertices):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for index_pair in indices:
        p1 = vertices[index_pair[0]]
        p2 = vertices[index_pair[1]]
        xs = [p1[0], p2[0]]
        ys = [p1[1], p2[1]]
        zs = [p1[2], p2[2]]
        ax.plot(xs, ys, zs, color="b")
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    plt.show()

rotated_vertices = rotate(vertices, 55, 45)  # Example angles
plot_cube(rotated_vertices)
